## Molecular representations with chemical meaning

Surfacia converts molecular surface properties into hierarchical descriptors and connects feature selection, machine learning and SHAP interpretation. It is intended for researchers who want to relate predictions to chemical structures.

## Workflow

- Prepare molecular structures from SMILES and organize quantum-chemical and surface-analysis tasks.
- Extract electrostatic potentials, local ionization energies and related surface descriptors.
- Select features, build models and interpret predictions.

## Installation and use

Install the Python package with `pip install surfacia` and run `surfacia --help`. Machine-learning analysis can also run separately on an existing descriptor table.

The full quantum-chemistry workflow additionally requires external tools such as xTB, Gaussian and Multiwfn, installed under their respective licenses. Consult the current documentation for environment and version requirements.

## Further information

Visit the [full documentation](https://surfacia.readthedocs.io/en/latest/) and [source repository](https://github.com/sym823808458/Surfacia) for commands, examples, dependencies and issue reporting.
