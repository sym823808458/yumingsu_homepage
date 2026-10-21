## From a spectrum image to numerical curves

## Online calculation

Use **Online compute demo** above, register with an email and password, verify your email and wait for administrator approval. In GBLine, upload a PNG or JPEG chart (up to 10 MiB), select the curve and point counts and submit. The server runs a fixed extraction workflow without external model calls. Review the calibration preview and diagnostics before downloading the curves. The online version supports one panel with one X/Y axis pair; uncertain extraction is flagged for review.

Each task is limited to 2 CPU threads, 4 GiB RAM and 5 minutes. All tools share 1 running task, 2 queued tasks and 10 daily submissions per user. Private results expire after 72 hours.

GBLine is a local tool for digitizing scientific line charts and chemical spectra. It connects OCR, coordinate calibration and pixel-based curve extraction with an optional vision-language-model review workflow through MCP.

The numerical core performs coordinate conversion and curve tracing. A visual model can inspect visible tick labels and curve colors, propose corrections and respond to the tool's diagnostic feedback.

## Main workflow

- Start with a single-panel chart and inspect the plotting area, axes and visible ticks.
- Establish a linear or log10 coordinate mapping from image evidence.
- Extract curve pixels; review ambiguous axes, missing curves or colors when requested.
- Retrieve full numerical curves and diagnostic records, then check coverage and numerical fidelity before reusing the data.

The MCP interface includes `inspect_chart_axes`, `extract_chart_data` and `get_curve_full_data`. Depending on the available evidence, the tool can return extracted data, request further review or abstain.

## What to check in the output

Correct axis calibration and the expected number of curves do not guarantee a complete trace. Inspect horizontal-domain coverage, gaps and the extracted curve against the source image. Multi-panel figures should be separated first; dual-y-axis plots and insufficient visible calibration evidence are outside the current workflow.

The research currently includes developmental and retrospective validation; independent evaluation on unseen spectra remains ongoing.

## Access and research status

The current local MCP implementation is documented as version 2.0.0. Model assistance requires a compatible image-capable agent and its selected provider; the numerical tool itself is not tied to a particular model service.

Contact Yuming Su for the current software and setup. A revised research manuscript is in preparation.
