# Content provenance — 2026-10-19

## Published research figures — 2026-10-20

At the author's request, the homepage's three research directions now pair the existing bilingual descriptions with published figures. No unpublished figures, instrument photos or new scientific results are used. Sources and exact image hashes are recorded in `images/research/README.md`.

- *Interpretable Machine Learning of Two-Photon Absorption*, Advanced Science (2023), DOI `10.1002/advs.202204902`: Fig. 4 for interpretable chemical ML and Fig. 2 for the two-photon absorption workflow. The Europe PMC full-text record `PMC10015897` identifies © 2023 The Authors and CC BY 4.0. Both figures are original to the article and have no separate third-party credit in their captions.
- *Automation and machine learning augmented by large language models in a catalysis study*, Chemical Science (2024), DOI `10.1039/d3sc07012c`: Fig. 1 for the overall information–experiment–computation workflow. Full text `PMC11304797` identifies CC BY-NC 3.0; this figure is used on the noncommercial academic homepage with attribution. Its caption has no third-party reproduction notice. The many separately credited third-party robot/platform figures elsewhere in this review were deliberately not reused. The homepage labels the selected figure as a review overview, not an instrument built or validated by the author.

The license and full captions were checked against the official Europe PMC full-text XML endpoints on 2026-10-20. Image bytes come from the NCBI CDN URLs present in the corresponding PMC article HTML and are stored unchanged. The webpage changes only their display size, preserves the whole figure, and provides source, figure number, license and DOI links. The original paper titles and image text remain in English in both language versions. Scholar statistics and the software catalogue are unchanged.

## Scholar snapshot

Yuming Su supplied a Google Scholar profile text in the website-maintenance conversation on 2026-10-19 (Asia/Shanghai).

| Metric | All time | Since 2021 |
| --- | ---: | ---: |
| Citations | 782 | 778 |
| h-index | 14 | 14 |
| i10-index | 15 | 15 |

The supplied list contains 20 scholarly records, not a confirmed total publication count. It includes 18 journal records, one arXiv preprint record and one MLatom software/resource record. Per-record citation counts come from that same supplied snapshot. No live Scholar synchronization is configured.

The 2026-10-19 display revision follows the author's preference for a ten-most-cited default and an optional chronological view. The paper section includes the 18 journal records and one preprint; the software/resource record remains in the data archive and is not ranked as a paper. No citation numbers, publication titles or dates were changed for this presentation update.

Scholar's account-management prompts, unverified-email notices, coauthor suggestions and open-access dashboard notices are not biography content and are excluded from the website.

The 2013 date of the MLatom resource is retained from the supplied record; it is not represented as a 2013 journal publication or as evidence of the author's employment in 2013.

## Biography and experience

- Existing `index.html` at commit `a50cbf7c96ce243b47403fe411c50794fa8dbe00`: name, education, position, lab, contact links and portrait.
- User-supplied current profile text: research keywords and Xiamen University / AI4EC Lab / IKKEM affiliation context.
- Local research summaries reviewed in this conversation: interpretable chemical ML, Surfacia/LoFFi, theoretical chemistry, electrochemistry and electroplating automation.

The website does not claim unverified grant totals, current publication totals, author-contribution roles, unreleased performance numbers or completion of planned experiments.

On 2026-10-19 the author supplied a new 886 × 1067 speaking photo and explicitly requested its use on the homepage. The supplied JPEG is copied unchanged to `images/profile.jpg`; the old portrait's magnification is removed. Both language versions share the same image with a content-hash query for cache invalidation. No retouching or generated replacement was applied.

## Public software sources

- https://github.com/sym823808458/Surfacia
- https://surfacia.readthedocs.io/zh-cn/latest/
- https://github.com/sym823808458/handle_candle
- https://github.com/sym823808458/pKaMLEducation
- https://doi.org/10.6084/m9.figshare.29755451
- https://github.com/sym823808458/calculateTPAbyMATLAB
- https://github.com/sym823808458/MultiwfnMLhelper

Software descriptions reflect the public README/documentation reviewed in this conversation. This update does not certify a fresh execution test of each software package.

The author subsequently requested that MultiwfnMLhelper no longer be displayed. Its entry is retained with `visible: false`; bilingual homepages omit it and former project URLs redirect to the corresponding software list. The upstream repository and software itself are unchanged.

On 2026-10-19 the author requested per-software historical visit counts and selected GoatCounter preparation. The integration follows the provider's official path override, counter JSON and session documentation. It remains disabled pending an owner-created site address. No historical visits, counts or account configuration have been invented; English/Chinese project pages share a stable per-project path.

On 2026-10-19 the author requested that the Surfacia introduction exclude the former Go Beyond extension. The local revision plan `D:/YumingSu/Papers/Surfacia/New_version_Surfacia_260826/00_project_control/05_完整研究计划_模型横向对比与数据划分.md` and the revision-scope statement in `06_manuscript/Surfacia_interpretability_SI_v7_structure_corrected.md` confirm that candidate acquisition, SPES and SHAP-cliff are outside the revised article. The website summary and bilingual project descriptions therefore focus on descriptors, modeling and interpretation. Local manuscripts, archived analyses and the separate Surfacia software/documentation repositories are not changed or uploaded by this website edit.

The subsequent authorized Surfacia repository/manual update is recorded separately in `sym823808458/Surfacia` at commit `16114d9007eb360728d1345aabb21105cf358fa8`. This homepage follow-up links its paired manual pages and distinguishes source revision from PyPI availability. Public examples use listed SMILES and RDKit-computed properties; they are not presented as unpublished catalytic results or a quantum-surface benchmark.

Surfacia 4.0.0 was published to [PyPI](https://pypi.org/project/surfacia/4.0.0/) on 2026-10-19. The version-specific PyPI JSON endpoint confirmed both wheel and source distribution, with SHA-256 hashes matching the locally checked release artifacts. Installation from the official PyPI index succeeded. The bilingual homepage installation text now directs users to the published release and explicitly upgrades older installations.

The Surfacia research preprint was verified against the live Crossref DOI record on 2026-10-19: DOI `10.26434/chemrxiv.15007949/v1`, title *Explain and Go Beyond with Surfacia: A Surface-Descriptor based Workflow for Interpretable Molecular Machine Learning*, authors Yuming Su, Yangtao Chen, Yiheng Dai and Cheng Wang, posted 2026-08-27, subtype `preprint`. The registered title is preserved verbatim, with an explicit note that this archived v1 predates the current scope revision. It is not treated as a software-release DOI or a journal acceptance. Citation counts and the dated Scholar list are unchanged.

## GBLine project page

Added at the author's request as the second visible software project, after Surfacia. The existing handle_candle project remains a separate entry. Sources reviewed:

- The user-referenced conversation `01a066e8-40b8-7531-860f-dfe29b486393`, including the 2026-10-16 first-draft delivery and the limits of retrospective/developmental validation.
- `D:/YumingSu/Papers/gbline/gbline-mcp/README.md` and `GBLINE_AUTO_MCP_V2.md`: the documented local 2.0.0 MCP interface, evidence correction, numerical extraction and abstention behavior.
- `D:/YumingSu/Papers/gbline/spectrum_project/paper_draft_v1_20261016/manuscript.md`: project positioning and remaining validation gaps.
- `D:/YumingSu/Papers/gbline/release_measurement_github_public_20260429/CITATION.cff`: an older release-manuscript title without a registered publication DOI.

No verified GBLine preprint was found in the Crossref title searches or public preprint searches on 2026-10-19. The page therefore describes a manuscript in preparation and does not invent a DOI, journal acceptance, public source URL or pip installation command. Public repository lookup was rate limited; absence of a repository is not claimed. The contact route is used pending a confirmed distribution link.

The workflow SVGs are newly authored schematics. No third-party article screenshots, manuscript figures, private spectra, API spending records or unverified benchmark claims were uploaded. This website update does not constitute a fresh GBLine extraction experiment.

## TPA Python and MATLAB workflow — 2026-10-20

### SOS theory attribution — 2026-10-20

At the author's request, the TPA software summary and paired detail pages explicitly identify the sum-over-states (SOS) framework. The current public `calculateTPAbyMATLAB/README.md`, retrieved from GitHub on 2026-10-20, names Terenziani et al., *Enhanced Two-Photon Absorption of Organic Chromophores: Theoretical and Experimental Assessments*, Advanced Materials 20, 4641–4678 (2008), DOI `10.1002/adma.200800402`, with the explicit note "theory comes from here". This review is identified as the direct method reference named by the workflow, not as the first discovery of SOS theory.

The public `calculateTPAinbatchpar.m` and the corrected-reference conversation's local `tpa_from_multiwfn.py` were read: both construct a frequency-dependent second-hyperpolarizability tensor from electronic energies and dipole products, include frequency permutations, state sums and damping, take an isotropic average, and use its imaginary part for the TPA cross section. This supports the high-level workflow description; it is not a certification of prefactors, permanent-dipole handling, convergence or Python/MATLAB equivalence. The known numerical review item recorded in `.work/tpa_python_review_20261020.md` remains unresolved and no calculation code or historical numerical result is changed by this content update. The public MATLAB script and shared Python companion also have different default damping values, so the webpage requires matched settings rather than claiming an identical common default.

Theory citations are separated by role: Orr and Ward (1971), Molecular Physics 20, 513–526, DOI `10.1080/00268977100100481`, for foundational perturbative nonlinear SOS response; Göppert-Mayer (1931), Annalen der Physik 401 [series volume 9], 273–294, DOI `10.1002/andp.19314010303`, for foundational two-photon transitions. Lu and Chen, Journal of Computational Chemistry 33, 580–592 (2012; online 2011), DOI `10.1002/jcc.22885`, is an upstream Multiwfn software citation. All four titles, author lists, volumes, pages and DOIs were checked against live Crossref records, with Wiley publisher records also checked for the 1931, 2008 and Multiwfn articles. The website preserves original reference titles in both languages. These method references are not added to Yuming Su's own publication list or citation statistics. Private input data, scripts and manuscripts remain unpublished.

The author corrected the reference conversation to `019f45e5-108c-7713-aa22-ebc2fba976f7`; the previously mentioned discussion is not used as evidence for this update. The corrected conversation records the collaborator-facing Python instructions and the prepared post-processing bundle.

Reviewed local sources under `D:/YumingSu/Papers/TPA/calc/tpa_batch_20260709/share/tpa_postprocess_bundle/`: `README_EN.md`, `python/tpa_from_multiwfn.py`, `python/requirements.txt`, `matlab/tpa_from_multiwfn.m` and the Multiwfn conversion helpers. The Python CLI accepts input/output directories and `--plot`; it writes spectrum CSVs, a summary and optional PNG plots. The CSV wavelength names are checked against the source and the corrected conversation: `lambda2_nm` is incident wavelength, `lambda_half_nm` is the one-photon-equivalent half wavelength.

The live public `sym823808458/calculateTPAbyMATLAB` repository was checked on 2026-10-20 and still presents the original MATLAB workflow. The updated website therefore describes both routes but identifies the public repository as MATLAB and offers the existing contact route for the separately shared Python companion. It does not invent a public Python repository, pip package or verified numerical equivalence.

This update publishes descriptions and generic usage commands only. The four molecules' private inputs, spectra, numerical results, server/account details and unpublished calculation logs from the conversation are not distributed. No new electronic-structure calculation or numerical-method validation is claimed.

## Publication metadata

The supplied titles, citation counts and years are the primary record of this update. DOI and bibliographic metadata were supplemented using existing public links, publisher records and Crossref. Successful Crossref checks are recorded per item with `metadata_source`, `metadata_checked` and `authors_verified`; HTTP 429 or other errors are not marked verified. User-supplied truncated author lists remain where no complete list has been confirmed. Preprint status is retained as supplied rather than inferring a later acceptance.

All publication links lead to the original scholarly resources. No full-text PDFs or copyrighted article images are republished.

## Building Wind Screening project page

Added on 2026-10-19 from the user-requested working folder `D:/YumingSu/Papers/buildings-analysis`:

- `wind_pressure_tool_product_brief.md`: project positioning, input/output workflow, known empirical assumptions, product ideas and future work. Product ideas are not treated as implemented features.
- `wind_pressure_requirements.md`: single-image annotation workflow and original-image coordinate convention.
- `wind_pressure_gui.py`: Python/Tkinter implementation; inspected functions include `pressure_result`, `save_project`, `load_project`, `export_plan_gif`, `export_3d_gif`, and `export_selected_output_png`.
- `1号楼-3d-wind.gif`: original 900 × 620, 36-frame software export, copied unchanged as the optional output animation. The displayed values are outputs of the simplified screening model, not validated design loads.

The bilingual workflow SVGs are newly authored schematics, not real-site maps or computed results. No site map images, saved annotation JSON, Python source code, commercial pricing proposals, or standalone HTML prototype were uploaded as part of this page. No formal paper manuscript was present in the reviewed folder, and no publication has been added for this project. The page presents a development prototype with a contact link; no public software repository or downloadable release has been invented.

## Surfacia online descriptor-table adapter — 2026-10-20

At the author's request, Surfacia was added to the isolated server queue alongside GBLine. The official PyPI 4.0.0 wheel was verified by SHA-256 against its version JSON record (06cd1090cb2ef0014d5d7c34ccc1d1914ba6a98eea2771e59f65c9393e57d02e); its `BaseChemMLAnalyzer.XGB_Fit` routine performs training. The web adapter uses a fixed grouped 80/20 holdout and five-fold GroupKFold validation, rather than claiming to execute the desktop CLI's repeated splits or the frozen article benchmark. No public package release or research archive was changed.

The public input is copied from `Surfacia-public/examples/descriptor_table/descriptors.csv`: 36 listed public SMILES, six RDKit descriptors and computed Crippen logP. Input SHA-256: 152f5c8ea6a6725c5cfe1309782a6f0a124b52bc6ef879270ab9062aaa596d93. A real browser submission completed server computation and authenticated ZIP download. The downloadable archive contains only that public tutorial's generated report, native model, CSVs and plots; no user account, session, credentials, server configuration or private research data is published. Its recorded metrics and package/source hashes are in report.json; signed SHAP values were independently checked against predictions. The displayed PNG is the actual held-out SHAP magnitude plot, not a manuscript figure.

The compute entry is a temporary Cloudflare Quick Tunnel. It may stop or change and is not represented as permanent compute.yumingsu.top hosting. On verification the owner had not yet configured QQ SMTP: new email registrations cannot complete until that configuration is supplied. Existing approved access worked. The public homepage's HTTP endpoint worked; HTTPS on yumingsu.top still had a certificate mismatch, which this content update does not claim to repair.

## Building wind direct-input web adapter — 2026-10-20

At the author's request, the existing private desktop wind-pressure calculation was exposed as a fixed, approved-account web task. A headless snapshot retains the original mathematical definitions and constants while removing GUI/image/export code. The original desktop source and saved site projects were not edited or published. Exact comparisons for 30 generated scenarios / 90 buildings matched the desktop source; 32 API/schema/physics tests passed locally and inside the guest. This establishes software equivalence, not physical validation.

A real HTTPS browser session entered the three synthetic rectangular buildings and one synthetic open area, submitted the task, viewed ranking/facade/height-band details, restored the result from task history and downloaded the archive. Overlapping geometry was rejected before consuming a job quota. Desktop/mobile layout and anonymous-result guards passed; Surfacia and GBLine were also rerun successfully on the same approved test tenant. The temporary test identity was disabled after verification. The public downloads and new height-band SVG contain only the synthetic scenario and generated outputs, with no real site image, geolocation, account, session or server configuration.

The JRC worked-examples wind-action text is linked only as general background for velocity-pressure/roughness concepts. The prototype's pressure-coefficient rules, clipping, band and environment factors are heuristic and are not claimed to implement or satisfy a design standard. Input speed is described as the model's reference scenario parameter because averaging-time/terrain normalization has not been calibrated. Results are nonnegative pressure magnitudes, not signed load cases or calibrated safety classes.

The entry remains an outbound temporary HTTPS tunnel. SMTP configuration and the permanent compute hostname remain pending, as on the Surfacia page. The software page's English/Chinese source files and shared data entry document these conditions.


## TPA Gaussian-pair web adapter — 2026-10-20

The dedicated compute VM now has a fourth fixed runner. The primary form accepts a Gaussian fchk and TD log, executes a pinned no-GUI Multiwfn binary and runs an AST snapshot of the already reference-fixed local `compute_tpa_from_multiwfn.py` (SHA256 `1deb1360a1d767935b2868b226004ec3daff2e72680f08560b61508ca27b3822`). This supersedes the earlier unresolved *reference-overwrite* note above: the local Python/MATLAB copies had already been repaired before this web adapter was built. No equality of the Python/MATLAB grids or absolute cross sections is certified, and historical outputs were not overwritten.

The pinned Multiwfn binary reports 3.8(dev), update 2024-10-20; its SHA256 is `73d191bfee733c3586f50cdbd358809e81ed381962e73a188c29e20d87135b42`. Its license permits component redistribution and is preserved in task downloads. The program asks for both the 2012 Multiwfn paper and Lu's 2024 JCP paper (DOI `10.1063/5.0216272`) to be cited in the main text; both are linked. The latter bibliographic record was checked against the publisher/Crossref-linked record. Terenziani/Orr-Ward/Göppert-Mayer remain the method and foundation references, separate from software citations.

A private, existing 12-atom / 192-basis / 20-state Gaussian pair was tested without publishing its files or molecular spectra. Fchk/log atom order, coordinates/frame, normal termination, excitation block, route export flag and available SCF energies are checked. ECP, open-shell, triplet, multi-block or unverified inputs are outside the supported service. A controlled rigid-coordinate translation diagnostic on that neutral sample supports total-ground/electronic-excited definitions for this pinned export; agreement is approximate at text-export precision. The original sample's computed nuclear moment is near zero, so the annotation alone is not used to assert a significant nuclear-contribution mixing error. All-electron nuclear charges and bohr coordinates provide the vector used to normalize permanent dipoles before the saved-reference subtraction.

The unaltered audited Python SOS equations produce negative response points on the private sample. They are preserved, shown with a prominent review flag, and are not advertised as validated absolute TPA predictions. This is a functioning preprocessing/postprocessing workflow, with physical validation of prefactors, finite-state convergence, damping and negative response still required. The denominator damping remains 0.05 eV; the legacy 0.528 Å conversion and frequency grid remain explicit. Input automation and the mu0-copy repair do not resolve every numerical or theoretical question.

Only an arbitrary two-excited-state algebra matrix is offered as a public loadable example. It is labeled synthetic, uses no private molecular data, and has no experimental meaning. Limits remain 2 CPU / 4 GiB / 10 minutes per TPA task, with the same approval, ownership, shared quotas, no-network container and 72-hour retention policy as the other tools. The temporary HTTPS endpoint and pending SMTP/permanent-domain status remain disclosed.

The public MATLAB repository still contained the overwrite loop on live inspection. Commit `f3eca3d` now saves `mu0` before subtraction and documents the narrow scope and remaining dipole-definition/physical-validation requirements. No MATLAB runtime validation is claimed. The online runner uses the separately audited Python snapshot.


### Input scope clarified — 2026-10-20

The owner subsequently requested only fchk + log. The text-upload route, manual dipole fields, route selector and loadable synthetic input were removed. Both the API metadata gate and isolated runner reject text-mode submissions. Historical synthetic numerical-check plots/results remain explicitly archival and are not an online input mode. Existing completed task downloads remain accessible under the original ownership/retention checks.

## Fixed compute portal — 2026-10-21

The operator completed Cloudflare DNS/tunnel setup. A fresh Edge browser verified https://compute.yumingsu.top with a valid certificate and HTTP 200. The encrypted tunnel forwards only to host loopback HTTP port 18080. The runtime canonical origin and all newly generated account email links were changed to this hostname; the old temporary URL is retained privately as a transition alias.

A temporary test applicant completed registration, password-protected email verification, authenticated administrator approval and password login through the fixed domain. Test emails were captured privately, not sent to example.net; the owner separately confirmed receipt of the QQ SMTP configuration email. Real isolated GBLine, Surfacia and wind tasks completed and downloaded; the matching Gaussian fchk/log TPA task returned review_required as expected and downloaded. Temporary applicant and acceptance administrator identities were disabled and their sessions revoked. Anonymous downloads and an unrelated request Origin were rejected. Desktop and mobile layouts passed. No scientific algorithm or limit changed.

## Authorship-prioritized publications — 2026-10-21

The author supplied six existing papers plus a seventh, newly added 19F NMR paper, explicitly identifying four co-first-author roles and one co-corresponding role; the two Su-first records are marked first author. These seven records are prioritized in the supplied order, followed by other papers by the existing citation snapshot. By-date controls and chronological JavaScript sorting are removed. All scholarly records and stable paper anchors remain in the generated archive; a deep link reveals only its hidden target.

The new article is *Improving Quantum-Chemical Prediction of 19F NMR Chemical Shifts via Machine Learning*, Journal of Chemical Information and Modeling 66 (17), 10538–10547 (2026), DOI https://doi.org/10.1021/acs.jcim.6c01056. The ACS article record and PubMed https://pubmed.ncbi.nlm.nih.gov/42734509/ confirm its full six-author list, year, issue and pages; ACS marks Yuming Su and Cheng Wang as corresponding authors. No citation count was supplied or verified for this addition, so it is null rather than zero. Existing citation counts and total metrics retain their previous dated snapshot. The site now archives 21 records (19 journal articles, one preprint, one software/resource); this is not a claim of the author’s complete publication count.

## Ground-reference audit synchronized — 2026-10-21

The author supplied the private 2026-10-20 comparison_report.txt plus CHANGELOG.txt and fix_verification.json. All four listed local MATLAB/Python copies and the public MATLAB loop already preserve the ground reference; the cloud core already uses an independent NumPy copy. Its scientific source bytes, equations, constants, grid and damping are unchanged by this update. New web adapter 1.0.2 adds the impact scope to report provenance and download documentation.

The bilingual TPA pages and public REFERENCE_FIX.md now report the four isolated 30-state main-peak changes (+0.009236%, +0.855914%, +0.784894%, −0.884634%) and the maximum non-main-peak relative change 10.722528%, measured among samples with old response ≥10% of old peak. The comparison changes only reference subtraction, not relaxed-density treatment or electronic/total definitions. It cannot justify a universal correction factor or negligible effects in all molecules. The private molecular inputs, numerical spectra and old output files are not published or overwritten.

## Cloudflare software-page counters — 2026-10-21

The owner created Worker/D1 `yumingsu-visits`, bound D1 as `DB`, initialized the fixed six-software schema and attached the corrected custom domain `stats.yumingsu.top`. Live HTTPS health and counts returned 200; the database start metadata is `2026-10-21T09:42:03Z`. Before frontend activation all six counters and the total were zero. These are initialized persisted counters, not reconstructed historical visits.

The unused GoatCounter scaffold is replaced with the author's public Worker API. English/Chinese homepages read the six software counters and their sum without creating visits. Visible detail pages send a fixed software slug and random UUID event, retained per software/tab for a 30-minute window; confirmations prevent refresh/language-switch writes, while uncertain retries reuse the same event ID. D1 insertion deduplication makes retries idempotent. Values shown are validated API aggregates, never client-generated totals. Hidden software and local previews do not call the service. Runtime failure displays unavailable, not a fabricated zero. No registration, secret, account or research input is needed to view or count these public pages.

Counter policy/normalization and ownership conditions are documented in MAINTENANCE.md. This is a page-visit metric, not unique people, downloads or completed computation. Production maintenance visits may count. Network-free regression and browser fixtures are isolated from the production database; screenshots with fixture values are not published as real metrics. The existing academic-domain certificate issue is tracked separately; the counter works from the existing HTTP site via the allowlisted Origin and HTTPS stats endpoint.
