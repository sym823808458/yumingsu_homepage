## From excited-state calculations to TPA analysis

This workflow uses **sum-over-states (SOS) theory** to calculate two-photon absorption (TPA) spectra and cross sections from electronic excitation energies and dipole matrix elements. It connects Gaussian excited-state calculations and Multiwfn transition-dipole extraction with **Python or MATLAB** post-processing.

## Theoretical basis: sum-over-states

In the electric-dipole approximation, SOS theory expresses the nonlinear optical response as sums over electronic states, using excitation energies, dipole matrix elements and frequency-dependent energy denominators. For degenerate TPA, two photons of the same frequency jointly supply the excitation energy; the intermediate-state sum describes virtual pathways, not two sequential real-state absorptions.

The post-processing code evaluates the frequency-dependent **second hyperpolarizability γ**, the molecular third-order optical response, with a finite set of supplied electronic states and phenomenological damping. It then uses the imaginary part of the isotropically averaged response to obtain the TPA spectrum and cross section in GM. The calculation follows the chain **excitation energies and dipoles → SOS response → orientational average → TPA cross section**. This is an electronic-structure-based calculation; the ML-TPA property-prediction models discussed in related publications are a separate route.

The original MATLAB repository identifies **Terenziani et al. (2008)** as its method reference. **Orr and Ward (1971)** provides the foundational perturbative SOS framework for nonlinear optical response; **Göppert-Mayer (1931)** is the foundational two-photon-transition paper. Full citations and DOI links are listed below.

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

The Python and MATLAB routes implement the existing post-processing workflow. Compare a known input when switching implementations; numerical equivalence has not been certified. A finite SOS state sum requires convergence checks. Report the electronic-structure method, basis set, solvent treatment, included states, dipole inputs and damping/broadening convention when comparing cross sections; peak heights are sensitive to broadening. Match these settings between implementations.

## Theory and software references

- **Direct method reference named by the original workflow:** F. Terenziani, C. Katan, E. Badaeva, S. Tretiak and M. Blanchard-Desce. [Enhanced Two-Photon Absorption of Organic Chromophores: Theoretical and Experimental Assessments](https://doi.org/10.1002/adma.200800402). Advanced Materials **20**, 4641–4678 (2008). DOI: `10.1002/adma.200800402`.
- **Foundational SOS response theory:** B. J. Orr and J. F. Ward. [Perturbation theory of the non-linear optical polarization of an isolated system](https://doi.org/10.1080/00268977100100481). Molecular Physics **20**, 513–526 (1971). DOI: `10.1080/00268977100100481`.
- **Foundational two-photon-transition theory:** M. Göppert-Mayer. [Über Elementarakte mit zwei Quantensprüngen](https://doi.org/10.1002/andp.19314010303). Annalen der Physik **401** [series volume 9], 273–294 (1931). DOI: `10.1002/andp.19314010303`.
- **Upstream wavefunction-analysis software:** T. Lu and F. Chen. [Multiwfn: A multifunctional wavefunction analyzer](https://doi.org/10.1002/jcc.22885). Journal of Computational Chemistry **33**, 580–592 (2012). DOI: `10.1002/jcc.22885`. Cite the Multiwfn version actually used, alongside the applicable Gaussian and electronic-structure-method references.

## Related research

This tool connects with research on machine learning of TPA, nanographenes and metal–organic layers. The [repository documentation](https://github.com/sym823808458/calculateTPAbyMATLAB) lists the related application papers. These complement the theory and upstream-software references above.
