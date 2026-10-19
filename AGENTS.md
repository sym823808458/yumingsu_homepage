# Website maintenance instructions

This repository is Yuming Su's existing public academic website on GitHub Pages.

- Read `README.md`, `MAINTENANCE.md` and `SOURCES.md` before editing.
- The user-authorized scope is personal biography, academic background, research software and scholarly publications.
- Edit Markdown and JSON content sources. Never patch generated `index.html` pages directly.
- Keep Chinese and English content aligned. Reuse the standard-library Python build and shared templates; avoid adding a framework or backend for routine changes.
- Run `python tools/build.py`, `python tools/build.py --check`, and `python tools/check_site.py`. Check desktop and mobile layouts for visual changes, and test publication controls if touched.
- Citation metrics and per-paper counts are dated snapshots. Do not invent a total publication count from an incomplete list. Separate journal articles, preprints and software resources.
- Do not publish internal experiment data, unreleased findings, credentials, equipment control interfaces or manuscript files without an explicit request covering them.
- Preserve project URLs and software slugs. Before removing a page, add a migration or redirect plan.
- Domain ownership and DNS must be verified before adding or changing `CNAME`; no domain has been bound as part of the 2026-10-19 update.
- Keep updates reviewable in Git. For an authorized publication, commit content sources and generated HTML together and verify the deployed site.
- Do not overwrite unrelated remote changes. Refresh the branch head before publishing and use a fast-forward or an expected-head lease.
- Do not add visitor counters or downloads badges with invented numbers. Analytics needs a real configured source.
