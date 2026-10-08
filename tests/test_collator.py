import pytest
from pypdf import PdfReader

from pdf_merger.core import PdfSource, collate_pdfs


@pytest.mark.skip(reason="collate_pdfs not implemented yet")
def test_collate_uneven_page_counts(make_pdf, tmp_path):
    a = make_pdf("a.pdf", 3)
    b = make_pdf("b.pdf", 1)
    out = tmp_path / "out.pdf"

    collate_pdfs([PdfSource(a), PdfSource(b)], out)

    assert len(PdfReader(out).pages) == 4
