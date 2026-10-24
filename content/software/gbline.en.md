## From a spectrum image to numerical curves

## Online calculation

Use **Online compute demo** above, register with an email and password, verify your email and wait for administrator approval. In GBLine, upload a PNG or JPEG chart (up to 10 MiB), enter the visible curve count and maximum point count, and submit once. A downloadable two-curve example is available in the workspace.

The workspace offers **pure software extraction** and a **Qwen-assisted** mode. When the site model service is configured and available, Qwen assistance is selected by default. It sends the chart image to the site-configured model provider for at most two reviews; the site supplies the key and covers model requests. Users do not enter an API key. Current availability is shown before submission; pure software remains available when the model service is not ready.

Open **Review curves** beside a completed task to compare the curves with the original image. Select, highlight or hide individual traces, zoom, and correct the result:

- Calibrate with two X ticks and two Y ticks. Enter the actual tick values and select linear or logarithmic axes; reversed axes are supported.
- Pick curve colors from the original raster, then re-extract with the corrections. This creates a new task under your normal quota and does not call Qwen.
- Erase unwanted points on the selected curve and undo strokes. Saved CSV files retain gaps using `segment_id`; do not reconnect separate segments.
- Save an accepted, needs-correction or abandoned review. Reopen saved versions and download their CSVs, overlay preview and review record. The original extraction remains a separate, unchanged download.

The online version supports one panel with one X/Y axis pair. A review-required result does not include certified numerical curves. Human calibration and acceptance are recorded as human interventions, not automatic validation. Model review cannot guarantee a correct extraction.

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

The current web adapter uses the selected `qwen-assist-2` policy and `compact-review-3` evidence checks. The local MCP implementation can also be used with a compatible image-capable agent. The numerical core is not tied to a particular model provider. Development examples do not establish accuracy on an independent test set.

Contact Yuming Su for the current software and setup. A revised research manuscript is in preparation.
