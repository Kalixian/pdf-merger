# PDF Merger

A simple desktop application for combining and collating PDF files.

- **Combine**: append PDFs one after another into a single file.
- **Collate**: interleave pages from multiple PDFs (e.g. merging separately
  scanned front and back pages).

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .[dev]
```

## Run

```powershell
python -m pdf_merger
```

## Test

```powershell
pytest
```

## Layout

```
src/pdf_merger/
    app.py            Application entry point
    core/             PDF logic (no GUI dependencies)
        models.py     Data types: PdfSource, PageRange, MergeMode
        merger.py     Sequential combine
        collator.py   Page interleaving
    gui/              tkinter user interface
        main_window.py
        widgets.py    Reusable widgets (file list, etc.)
tests/                pytest tests for core/
```
