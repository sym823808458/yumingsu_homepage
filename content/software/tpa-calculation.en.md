## From excited-state calculations to TPA analysis

This workflow connects Gaussian excited-state calculations and Multiwfn transition-dipole extraction with **Python or MATLAB** post-processing for two-photon absorption (TPA) spectra and cross sections.

## Three steps

- Complete a Gaussian TD calculation and convert its checkpoint to `.fchk` with `formchk`.
- Export the transition-dipole text with Multiwfn and save one named `.txt` file per molecule.
- Choose Python or MATLAB to process the same type of exported data and generate numerical spectra.

## Python companion

The existing `tpa_from_multiwfn.py` companion reads Multiwfn text containing the ground-state dipole, ground-to-excited and excited-to-excited transition moments, and excitation energies. Its input is the exported transition-dipole text, rather than a raw Gaussian log.

After obtaining the Python companion through the contact link above:

- Create an environment: `conda create -n tpa python=3.11`, then `conda activate tpa`.
- Install the two dependencies: `python -m pip install numpy matplotlib`.
- Put the exported files in `tpa_inputs` beside the script, and run `python tpa_from_multiwfn.py --input-dir tpa_inputs --output-dir tpa_outputs --plot`.

It writes `tpa_summary.csv`, one `*_tpa_spectrum.csv` per molecule, and optional PNG spectra under `plots/`. Python post-processing does not require MATLAB; generating new electronic-structure and dipole inputs still requires the upstream chemistry tools.

## MATLAB route

The [public MATLAB repository](https://github.com/sym823808458/calculateTPAbyMATLAB) provides Gaussian and Multiwfn examples, `batchTDM.bat`, and `calculateTPAinbatchpar.m`. It remains the public source entry for the original workflow; the Python companion is currently shared separately by enquiry.

## Reading and comparing results

In the Python output, `sigma_gm` is the calculated cross section in GM. `lambda2_nm` is the incident wavelength for degenerate two-photon excitation; `lambda_half_nm` is half that value, the one-photon-equivalent wavelength. Keep these conventions explicit when plotting or reporting a peak.

The Python and MATLAB routes implement the existing post-processing workflow. Compare a known input when switching implementations; numerical equivalence has not been certified. Results depend on the supplied electronic states, transition moments, state range and broadening parameters.

## Related research

This tool connects with research on machine learning of TPA, nanographenes and metal–organic layers. See the [repository documentation](https://github.com/sym823808458/calculateTPAbyMATLAB) for methodology and citations.
