# Website maintenance instructions

This repository is Yuming Su's existing public academic website on GitHub Pages.

- Read `README.md`, `MAINTENANCE.md` and `SOURCES.md` before editing.
- The user-authorized scope is personal biography, academic background, research software and scholarly publications.
- Edit Markdown and JSON content sources. Never patch generated `index.html` pages directly.
- Keep Chinese and English content aligned. Reuse the standard-library Python build and shared templates; avoid adding a framework or backend for routine changes.
- English is the default at the site root and `/software/<slug>/`. Chinese lives under `/zh/` with a visible language switch. Preserve `/en/` compatibility redirects. Keep paper titles, authors, journal names and DOI in their original language; the user explicitly does not want Chinese paper-title translations.
- Use Times New Roman as the primary English font, with system serif fallbacks for Chinese. Keep the original portrait and its CSS framing aligned with the identity block. Publications default to the ten most cited journal/preprint records, with a chronological view for all listed papers. Preserve the full data archive and links to individual papers.
- Run `python tools/build.py`, `python tools/build.py --check`, and `python tools/check_site.py`. Check desktop and mobile layouts for visual changes, and test publication controls if touched.
- Citation metrics and per-paper counts are dated snapshots. Do not invent a total publication count from an incomplete list. Separate journal articles, preprints and software resources.
- Do not publish internal experiment data, unreleased findings, credentials, equipment control interfaces or manuscript files without an explicit request covering them.
- Preserve project URLs and software slugs. Before removing a page, add a migration or redirect plan.
- Domain ownership and DNS must be verified before adding or changing `CNAME`. The configured custom domain is `yumingsu.top`; preserve the root `CNAME` file during content updates. Its four GitHub Pages A records and GitHub ownership-challenge TXT record were confirmed live on 2026-10-19.
- Keep updates reviewable in Git. For an authorized publication, commit content sources and generated HTML together and verify the deployed site.
- Do not overwrite unrelated remote changes. Refresh the branch head before publishing and use a fast-forward or an expected-head lease.
- Do not add visitor counters or downloads badges with invented numbers. Analytics needs a real configured source.
