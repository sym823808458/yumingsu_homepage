## From excited-state calculations to TPA analysis

This workflow connects Gaussian, Multiwfn and MATLAB to extract transition dipole information and perform batch two-photon absorption (TPA) calculations and analysis.

## Three steps

- Calculate excited states with Gaussian and prepare the required output files.
- Extract transition dipole information with Multiwfn.
- Process the extracted data and calculate TPA with MATLAB.

## Repository contents

The repository includes a Gaussian input example, a Multiwfn output example, the `batchTDM.bat` batch script and the `calculateTPAinbatchpar.m` MATLAB program.

## Requirements

Users need their own Gaussian, Multiwfn and MATLAB environments. Results depend on the theoretical method, excited-state range and parameters; consult the original methodology and repository references.

## Related research

This tool connects with research on machine learning of TPA, nanographenes and metal–organic layers. See the [repository documentation](https://github.com/sym823808458/calculateTPAbyMATLAB) for methodology and citations.
