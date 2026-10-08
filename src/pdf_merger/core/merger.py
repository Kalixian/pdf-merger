"""Sequentially combine PDFs into a single output file."""

from pathlib import Path

from pdf_merger.core.models import PdfSource


def combine_pdfs(sources: list[PdfSource], output_path: Path) -> None:
    """Write every selected page of each source, in order, to ``output_path``."""
    raise NotImplementedError
