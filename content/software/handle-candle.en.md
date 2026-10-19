## Literature research driven by scientific questions

handle_candle is a local Windows literature research tool. It opens paper pages in Edge and sends available page content to a language model for analysis, supporting iterative, traceable investigations.

## Main workflow

- Search and evaluate literature around a scientific question.
- Read accessible page content and organize structured analysis.
- Expand through citation relationships and retain URLs, logs and reports.
- Use Zotero to organize and download literature the user is authorized to access.

## Running locally

Download the repository, install `requirements.txt`, and launch `python modular_research_gui.py`. Use `python pdf_analysis_gui.py` for PDF-folder analysis.

Requirements include Windows, Microsoft Edge, Python and the selected model service. The PDF download workflow requires Zotero. Model calls may incur provider charges; full-text access depends on the user's existing permissions.

## Source and feedback

The [source repository](https://github.com/sym823808458/handle_candle) includes installation scripts, usage instructions and issue reporting.
