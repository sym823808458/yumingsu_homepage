(() => {
  const languageSwitch = document.querySelector('.language-link');
  if (languageSwitch) languageSwitch.addEventListener('click', event => {
    if (event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    const target = new URL(languageSwitch.href);
    target.hash = location.hash;
    location.assign(target.href);
  });
  const list = document.querySelector('[data-publications]');
  if (!list) return;
  const tabs = [...document.querySelectorAll('[data-publication-view]')];
  const rows = [...list.querySelectorAll('[data-publication]')];
  const count = document.getElementById('publication-count');
  let mode = 'citations';
  function update() {
    const ordered = [...rows].sort((a, b) => mode === 'citations'
      ? Number(b.dataset.citations) - Number(a.dataset.citations) || Number(b.dataset.year) - Number(a.dataset.year)
      : Number(b.dataset.year) - Number(a.dataset.year) || Number(b.dataset.citations) - Number(a.dataset.citations));
    let visible = 0;
    for (const [index, row] of ordered.entries()) {
      row.hidden = mode === 'citations' && index >= 10;
      if (!row.hidden) visible++;
      list.append(row);
    }
    const template = mode === 'citations' ? count.dataset.templateTop : count.dataset.templateTime;
    count.textContent = template.replace('{count}', visible);
    for (const tab of tabs) tab.setAttribute('aria-pressed', String(tab.dataset.publicationView === mode));
  }
  for (const tab of tabs) tab.addEventListener('click', () => {
    mode = tab.dataset.publicationView;
    update();
  });
  for (const tab of tabs) tab.disabled = false;
  // Project pages can link to a paper outside the default top ten.
  function revealLinkedPaper() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = rows.find(row => row.id === id);
    if (!target) return;
    if (target.hidden) { mode = 'year'; update(); }
    requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
  }
  window.addEventListener('hashchange', revealLinkedPaper);
  update();
  revealLinkedPaper();
})();
