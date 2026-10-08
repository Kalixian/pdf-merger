"""Core PDF operations. This package must not import any GUI code."""

from pdf_merger.core.collator import collate_pdfs
from pdf_merger.core.merger import combine_pdfs
from pdf_merger.core.models import MergeMode, PageRange, PdfSource

__all__ = ["MergeMode", "PageRange", "PdfSource", "collate_pdfs", "combine_pdfs"]
