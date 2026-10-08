"""Interleave pages from multiple PDFs into a single output file."""

from pathlib import Path

from pdf_merger.core.models import PdfSource


def collate_pdfs(sources: list[PdfSource], output_path: Path) -> None:
    """Write pages round-robin (A1 B1 A2 B2 ...) to ``output_path``.

    When sources have different page counts, the remaining pages of the
    longer sources are appended once the shorter ones run out.
    """
    raise NotImplementedError
