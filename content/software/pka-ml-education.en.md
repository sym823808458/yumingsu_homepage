## Learning machine learning through a familiar chemical problem

pKa-ML Education introduces decision trees, feature engineering and generalization through organic acid pKa prediction. The online teaching workspace runs without installing Python; the original desktop GUI remains available.

## Try an interactive lesson

1. Open the [free online workspace](https://compute.yumingsu.top/?tool=pka) and sign in with an approved account.
2. Choose one of five public teaching datasets, select descriptors and set maximum tree depth (1–10; default 3). Preview or download the data before submitting.
3. Compare training and validation MAE, RMSE and R² with the training-mean baseline. The four diagnostic molecules are shown separately.
4. Click a molecule on the parity plot or choose its name. Follow each inequality to its predicted leaf value; expand the complete tree to see the highlighted path.
5. Edit numeric descriptors for an immediate local what-if prediction. Download that prediction as CSV, or download the complete server result ZIP. Reload the lesson settings to submit a different model.

The depth-comparison plot uses the same split for depths 1–10, helping students discuss overfitting. Feature importance describes this tree’s splits; it does not establish a chemical mechanism or causal effect.

## Five datasets and visible representations

- Module 1 starts with carbon and carboxyl counts.
- Module 2 adds halogen counts.
- Module 3 uses more detailed atom and group counts.
- Module 4 retains those counts and adds EWG position and flag fields; descriptor selection is explicit.
- Module 5 uses carbon/carboxyl counts, EWG position and EWG rank.

The public CSV values are preserved. EWG rank codes span −1 to 9 and are not a continuous physical constant; use the preview table because the desktop tooltip omits some codes. Modules can differ in both molecules and descriptors, so not every comparison isolates one variable.

## A teaching diagnostic panel, not a blind test

Octanoic acid, 3-chlorobutanoic acid, iodoacetic acid and phenylglyoxylic acid are removed before training/validation splitting. Their labels are repeatedly displayed during teaching, so their results are a diagnostic panel rather than an independent blind external evaluation.

The web adapter uses all remaining rows in source order, with an integer floor(20%) validation size and split seed 42. A decision-tree regressor uses seed 1 and the selected depth/features. Repeated tuning against the same validation set does not give an unbiased final score. This small teaching model does not infer descriptors from SMILES, estimate uncertainty or establish general pKa accuracy. Manually edited descriptors may not describe a chemically valid molecule.

## Outputs and limits

The ZIP contains source data, predictions and split membership, the depth comparison, tree nodes, metrics, provenance and instructions. Adapter 1.0.0 uses the public repository snapshot `f9735619f4e4517bf70a7f4d0ba44a831286827e`. A reproducibility example with module 5, all four descriptors and depth 3 has 34 training, 8 validation and 4 diagnostic molecules; validation MAE is approximately 0.469 pKa. This is an example run, not an accuracy benchmark.

Each server task is limited to 1 CPU, 1 GiB memory and two minutes. The shared approved-account allowance is one running task, two queued tasks and ten submissions per day. Results are retained for 72 hours. Subsequent browser what-if edits do not submit new tasks. No user scripts, models or custom training-data uploads are accepted in this version.

## Desktop version

Windows users can obtain an executable from [figshare](https://doi.org/10.6084/m9.figshare.29755451). Python users can run `python DTcode/predictpka260324.py`; consult the [public repository](https://github.com/sym823808458/pKaMLEducation) for dependencies and citation updates. The desktop GUI also supports row selection; the web version deliberately uses the complete modeling pool.
