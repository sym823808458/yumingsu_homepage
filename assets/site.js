(() => {
  const list = document.querySelector('[data-publications]');
  if (!list) return;
  const search = document.getElementById('publication-search');
  const year = document.getElementById('publication-year');
  const sort = document.getElementById('publication-sort');
  const tabs = [...document.querySelectorAll('[data-publication-mode]')];
  const rows = [...list.querySelectorAll('[data-publication]')];
  const count = document.getElementById('publication-count');
  const empty = document.getElementById('publication-empty');
  let mode = 'all';
  function update() {
    const term = search.value.trim().toLocaleLowerCase();
    const ordered = [...rows].sort((a, b) => sort.value === 'citations'
      ? Number(b.dataset.citations) - Number(a.dataset.citations) || Number(b.dataset.year) - Number(a.dataset.year)
      : Number(b.dataset.year) - Number(a.dataset.year) || Number(b.dataset.citations) - Number(a.dataset.citations));
    let visible = 0;
    for (const row of ordered) {
      row.hidden = !((mode !== 'selected' || row.dataset.featured === 'true') &&
        (!year.value || row.dataset.year === year.value) &&
        (!term || row.dataset.search.includes(term)));
      if (!row.hidden) visible++;
      list.append(row);
    }
    count.textContent = count.dataset.template.replace('{count}', visible).replace('{total}', rows.length);
    empty.hidden = visible !== 0;
  }
  for (const tab of tabs) tab.addEventListener('click', () => {
    mode = tab.dataset.publicationMode;
    for (const candidate of tabs) candidate.setAttribute('aria-pressed', String(candidate === tab));
    update();
  });
  search.addEventListener('input', update);
  year.addEventListener('change', update);
  sort.addEventListener('change', update);
  update();
})();
