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
  const rows = [...list.querySelectorAll('[data-publication]')];
  const count = document.getElementById('publication-count');
  // Keep the authored priority order, revealing only a directly linked archived paper.
  function revealLinkedPaper() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = rows.find(row => row.id === id);
    if (!target) return;
    if (target.hidden) {
      target.hidden = false;
      count.textContent = count.dataset.template.replace('{count}', rows.filter(row => !row.hidden).length);
    }
    requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
  }
  window.addEventListener('hashchange', revealLinkedPaper);
  revealLinkedPaper();
})();
