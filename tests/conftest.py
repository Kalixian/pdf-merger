"""Shared pytest fixtures."""

from pathlib import Path

import pytest
from pypdf import PdfWriter


@pytest.fixture
def make_pdf(tmp_path: Path):
    """Return a factory that writes a blank PDF with ``pages`` pages."""

    def _make(name: str, pages: int) -> Path:
        writer = PdfWriter()
        for _ in range(pages):
            writer.add_blank_page(width=612, height=792)
        path = tmp_path / name
        with path.open("wb") as f:
            writer.write(f)
        return path

    return _make
