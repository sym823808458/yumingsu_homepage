## Molecular representations with chemical meaning

Surfacia converts molecular surface properties into hierarchical descriptors and connects feature selection, machine learning and SHAP interpretation. It is intended for researchers who want to relate predictions to chemical structures.

## Workflow

- Prepare molecular structures from SMILES and organize quantum-chemical and surface-analysis tasks.
- Extract electrostatic potentials, local ionization energies and related surface descriptors.
- Select features, build models and interpret predictions.

## Run a descriptor table on the server

Use **Online compute demo** above. Approved users can submit Surfacia tasks through the same account as GBLine. The temporary HTTPS address may change. New-user email verification still awaits the owner's QQ SMTP setup; an existing approved account can use the compute service.

- Download the example CSV from the compute page, or prepare your own UTF-8 CSV. Include one continuous numeric `target` column and 1–32 numeric descriptor columns. Use 30–500 samples and a file of at most 2 MiB. Descriptor names begin with an English letter and use letters, digits and underscores; no missing values, infinities or formulas.
- An optional `Sample Name` column stores unique identifiers (letters, digits, dots, underscores and hyphens, beginning with a letter or digit). If omitted, row numbers are used. Optional `smiles` are accepted as text and ignored by this online calculation; all other columns must be numeric descriptors.
- Register with an email and password, verify the email and wait for administrator approval. Sign in, select **Surfacia**, upload the CSV and submit. Save the task ID; you can close the page and return later.
- Download the ZIP when the task completes. Start with `README.txt` and `report.json`, then inspect `predictions.csv` and `parity.png`. Compare held-out MAE, RMSE and R² with the training-mean baseline before interpreting features.
- Read `feature_importance.csv` / `shap_importance.png` for attribution magnitude. `shap_values.csv` preserves descriptor values and signed contributions for held-out samples; `shap_dependence.png` shows the leading descriptor's direction. SHAP describes a fitted model, not a verified mechanism or causal intervention.

Each user shares one running task, two queued tasks and ten daily submissions across both tools. Surfacia runs have a ten-minute time limit. Results are private to the submitting account and removed after 72 hours; download them promptly.

### What the online analysis computes

The server calls Surfacia 4.0.0's `BaseChemMLAnalyzer.XGB_Fit` routine with all uploaded descriptors and fixed XGBoost regression settings (350 trees, depth 8, learning rate 0.03, CPU only). It accepts data, with no uploaded scripts or models.

A fixed seed of 42 holds out 20% of distinct descriptor vectors; identical vectors remain together. Five-fold grouped validation predicts every modeling-pool sample once out of fold. A final model fitted on that pool predicts the untouched held-out samples, where signed TreeSHAP contributions are also computed and their additivity is checked. There is no feature search, hyperparameter tuning, early stopping or test-driven selection. The archive records parameters, feature order, package versions, input/source hashes, split membership and the final native XGBoost `model.json`.

This bounded web protocol differs from the desktop CLI's repeated random splits and from the article's frozen research benchmark. A random grouped split does not replace scaffold, chronological or external validation. Full molecular structure preparation, quantum chemistry, surface extraction and interactive 3D viewing remain in the local workflow.

### Recorded online example

On 20 October 2026 the public 36-molecule CSV completed a real web submission, background computation and ZIP download. Twenty-eight modeling samples had out-of-fold R² 0.776 and MAE 0.259; eight held-out samples had R² 0.858, MAE 0.181 and RMSE 0.275. The held-out training-mean baseline RMSE was 0.762. SHAP contributions reconstructed predictions within 3.6 × 10⁻⁷.

[Download the example CSV](http://yumingsu.top/downloads/surfacia/descriptors.csv) and [recorded output archive](http://yumingsu.top/downloads/surfacia/online-demo-results.zip). The example uses six RDKit descriptors and **computed Crippen logP**, not experimental labels or quantum surface descriptors. The small test set and different validation protocol prevent direct performance comparison with the desktop tutorial. Feature ranks describe this run only.

## Installation and use

Install the current version from PyPI using the command above, then run `surfacia --help`. Machine-learning analysis can also run separately on an existing descriptor table.

Version 4.0.0 is available on PyPI and focuses on descriptors, modeling and interpretation. If you installed 3.0.3 previously, use the upgrade command above and check the manual's migration notes. Follow the [worked explanation](https://surfacia.readthedocs.io/zh-cn/latest/examples/interpretation.html) from a sulfur-local chemical question to an evidence card, and inspect the downloadable teaching run's signed SHAP outputs.

The full quantum-chemistry workflow additionally requires external tools such as xTB, Gaussian and Multiwfn, installed under their respective licenses. Consult the current documentation for environment and version requirements.

## Research preprint

Yuming Su, Yangtao Chen, Yiheng Dai and Cheng Wang. **Explain and Go Beyond with Surfacia: A Surface-Descriptor based Workflow for Interpretable Molecular Machine Learning.** ChemRxiv, v1, 27 August 2026. [DOI: 10.26434/chemrxiv.15007949/v1](https://doi.org/10.26434/chemrxiv.15007949/v1).

This archived preprint predates the current 4.0.0 scope revision and the latest interpretability-focused manuscript. Its registered title is retained verbatim; it is not a current feature list or a journal acceptance.

## Documentation and source

Visit the [full documentation](https://surfacia.readthedocs.io/zh-cn/latest/) and [source repository](https://github.com/sym823808458/Surfacia) for commands, examples, dependencies and issue reporting.
