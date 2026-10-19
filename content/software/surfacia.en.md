## Molecular representations with chemical meaning

Surfacia converts molecular surface properties into hierarchical descriptors and connects feature selection, machine learning and SHAP interpretation. It is intended for researchers who want to relate predictions to chemical structures.

## Workflow

- Prepare molecular structures from SMILES and organize quantum-chemical and surface-analysis tasks.
- Extract electrostatic potentials, local ionization energies and related surface descriptors.
- Select features, build models and interpret predictions.

## Installation and use

Install the current version from PyPI using the command above, then run `surfacia --help`. Machine-learning analysis can also run separately on an existing descriptor table.

Version 4.0.0 is available on PyPI and focuses on descriptors, modeling and interpretation. If you installed 3.0.3 previously, use the upgrade command above and check the manual's migration notes. Follow the [worked explanation](https://surfacia.readthedocs.io/zh-cn/latest/examples/interpretation.html) from a sulfur-local chemical question to an evidence card, and inspect the downloadable teaching run's signed SHAP outputs.

The full quantum-chemistry workflow additionally requires external tools such as xTB, Gaussian and Multiwfn, installed under their respective licenses. Consult the current documentation for environment and version requirements.

## Research preprint

Yuming Su, Yangtao Chen, Yiheng Dai and Cheng Wang. **Explain and Go Beyond with Surfacia: A Surface-Descriptor based Workflow for Interpretable Molecular Machine Learning.** ChemRxiv, v1, 27 August 2026. [DOI: 10.26434/chemrxiv.15007949/v1](https://doi.org/10.26434/chemrxiv.15007949/v1).

This archived preprint predates the current 4.0.0 scope revision and the latest interpretability-focused manuscript. Its registered title is retained verbatim; it is not a current feature list or a journal acceptance.

## Documentation and source

Visit the [full documentation](https://surfacia.readthedocs.io/zh-cn/latest/) and [source repository](https://github.com/sym823808458/Surfacia) for commands, examples, dependencies and issue reporting.
