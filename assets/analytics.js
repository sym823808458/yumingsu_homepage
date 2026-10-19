// A public GoatCounter endpoint is sufficient. Never put an API token here.
(() => {
  const root = document.body;
  const endpoint = root.dataset.analyticsEndpoint;
  const hosts = (root.dataset.analyticsHosts || '').split(',');
  if (!endpoint || !hosts.includes(location.hostname)) return;
  if (!/^https:\/\/[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.goatcounter\.com$/.test(endpoint)) return;

  const zh = document.documentElement.lang.startsWith('zh');
  const failed = zh ? '暂时无法读取' : 'Temporarily unavailable';
  // A build-defined stable path combines English/Chinese pages for each project,
  // independent of the domain, /index.html, query strings or fragments.
  const path = root.dataset.analyticsPath;
  const title = root.dataset.analyticsTitle;
  window.goatcounter = {path, title};
  const tracker = document.createElement('script');
  tracker.async = true;
  tracker.src = 'https://gc.zgo.at/count.js';
  tracker.dataset.goatcounter = endpoint + '/count';
  document.head.appendChild(tracker);

  const requests = new Map();
  for (const node of document.querySelectorAll('[data-visit-count]')) {
    const key = node.dataset.visitCount;
    if (!requests.has(key)) {
      requests.set(key, fetch(endpoint + '/counter/' + encodeURIComponent(key) + '.json', {
        credentials: 'omit', referrerPolicy: 'no-referrer', signal: AbortSignal.timeout(8000)
      }).then(response => {
        if (!response.ok) throw new Error('Counter is not available');
        return response.json();
      }).then(data => {
        const value = String(data.count);
        if (!/^\d[\d,\s.]*$/.test(value) || value.length > 30) throw new Error('Invalid counter');
        return value;
      }));
    }
    requests.get(key).then(value => { node.textContent = value; })
      .catch(() => { node.textContent = failed; });
  }
})();
