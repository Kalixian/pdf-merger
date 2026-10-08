import pytest
from pypdf import PdfReader

from pdf_merger.core import PdfSource, combine_pdfs


@pytest.mark.skip(reason="combine_pdfs not implemented yet")
def test_combine_page_count(make_pdf, tmp_path):
    a = make_pdf("a.pdf", 2)
    b = make_pdf("b.pdf", 3)
    out = tmp_path / "out.pdf"

    combine_pdfs([PdfSource(a), PdfSource(b)], out)

    assert len(PdfReader(out).pages) == 5
