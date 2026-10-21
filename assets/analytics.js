// Public aggregate counts only; no keys, accounts, cookies or personal identifiers.
(() => {
  'use strict';
  const root = document.body;
  const endpoint = root.dataset.analyticsEndpoint;
  const hosts = (root.dataset.analyticsHosts || '').split(',');
  if (root.dataset.analyticsProvider !== 'cloudflare-d1' || endpoint !== 'https://stats.yumingsu.top' || !hosts.includes(location.hostname)) return;
  const software = new Set(['surfacia', 'gbline', 'handle-candle', 'pka-ml-education', 'tpa-calculation', 'building-wind-screening']);
  const slug = root.dataset.analyticsSoftware;
  const minutes = Number(root.dataset.analyticsMinutes);
  if (minutes !== 30 || (slug && !software.has(slug))) return;
  const zh = document.documentElement.lang.startsWith('zh');
  const failed = zh ? '暂时无法读取' : 'Temporarily unavailable';
  const nodes = document.querySelectorAll('[data-visit-count], [data-visit-total]');
  const uuidPattern = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

  function uuid() {
    // getRandomValues also works on the current HTTP homepage; randomUUID may not.
    const bytes = crypto.getRandomValues(new Uint8Array(16));
    bytes[6] = (bytes[6] & 15) | 64;
    bytes[8] = (bytes[8] & 63) | 128;
    const hex = Array.from(bytes, b => b.toString(16).padStart(2, '0')).join('');
    return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`;
  }

  function visitRecord() {
    if (!slug) return null; // The homepage reads totals without submitting visits.
    try {
      const key = 'software-visit:v1:' + slug;
      const now = Date.now();
      const saved = JSON.parse(sessionStorage.getItem(key) || 'null');
      if (saved && uuidPattern.test(saved.id) && Number.isFinite(saved.at) && saved.at <= now && now - saved.at < minutes * 60000) {
        return {key, value: saved};
      }
      const value = {id: uuid(), at: now, confirmed: false};
      // Save before sending so reloads and uncertain network retries reuse the ID.
      sessionStorage.setItem(key, JSON.stringify(value));
      return {key, value};
    } catch {
      // Without storage/randomness we cannot deduplicate reloads: read only.
      return null;
    }
  }

  function validate(data) {
    if (!data || !data.counts || Object.keys(data.counts).sort().join(',') !== [...software].sort().join(',') || !Number.isSafeInteger(data.total) || data.total < 0 || typeof data.started_at !== 'string' || !/^\d{4}-\d{2}-\d{2}T/.test(data.started_at)) throw new Error('Invalid counter response');
    let total = 0;
    for (const name of software) {
      const value = data.counts[name];
      if (!Number.isSafeInteger(value) || value < 0) throw new Error('Invalid persisted count');
      total += value;
    }
    if (!Number.isSafeInteger(total) || total !== data.total) throw new Error('Inconsistent total');
    return data;
  }

  async function request(path, options = {}) {
    const response = await fetch(endpoint + path, {
      credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store',
      signal: AbortSignal.timeout(8000), ...options
    });
    if (!response.ok) throw new Error('Counter unavailable');
    return validate(await response.json());
  }

  async function counts() {
    const record = visitRecord();
    if (record && record.value.confirmed !== true) {
      try {
        const data = await request('/v1/visit', {
          method: 'POST', headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({software: slug, event_id: record.value.id})
        });
        try {
          sessionStorage.setItem(record.key, JSON.stringify({...record.value, confirmed: true}));
        } catch { /* The saved event ID still makes a retry idempotent. */ }
        return data;
      } catch { /* Leave the ID unconfirmed and reuse it on the next visit. */ }
    }
    return request('/v1/counts');
  }

  counts().then(data => {
    const format = new Intl.NumberFormat(zh ? 'zh-CN' : 'en');
    for (const node of nodes) {
      const value = node.hasAttribute('data-visit-total') ? data.total : data.counts[node.dataset.visitCount];
      node.textContent = Number.isSafeInteger(value) ? format.format(value) : failed;
    }
  }).catch(() => {
    for (const node of nodes) node.textContent = failed;
  });
})();
