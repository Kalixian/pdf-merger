import pytest

from pdf_merger.core import PageRange


@pytest.mark.skip(reason="PageRange.parse not implemented yet")
def test_parse_page_ranges():
    assert PageRange.parse("1-3, 5, 8-") == [
        PageRange(1, 3),
        PageRange(5, 5),
        PageRange(8, None),
    ]
