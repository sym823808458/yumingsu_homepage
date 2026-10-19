## Turning quantum-chemical results into feature matrices

MultiwfnMLhelper is a Python helper that organizes batch Multiwfn descriptor extraction and collects the results into a CSV table for machine learning.

## Input and output

- Input: a collection of Gaussian formatted checkpoint (`.fchk`) files.
- Analysis: Python and batch parameter files organize Multiwfn operations.
- Output: a CSV matrix of molecular descriptors.

## Getting started

Obtain `MultiwfnMLhelper.py`, the batch script and parameter files from the [repository](https://github.com/sym823808458/MultiwfnMLhelper). Install the required Python dependencies and obtain Multiwfn separately, then follow the configuration instructions.

## Scope

The tool prepares descriptors from existing wavefunction calculation outputs. It does not replace quantum-chemical calculations or Multiwfn itself. Consult the original Multiwfn documentation for descriptor definitions and analysis methods.
