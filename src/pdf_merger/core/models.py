"""Data types shared by the core and GUI layers."""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class MergeMode(Enum):
    COMBINE = "combine"  # A1 A2 A3 B1 B2 B3
    COLLATE = "collate"  # A1 B1 A2 B2 A3 B3


@dataclass
class PageRange:
    """A 1-based, inclusive page range. ``end=None`` means through the last page."""

    start: int = 1
    end: int | None = None

    @classmethod
    def parse(cls, text: str) -> list["PageRange"]:
        """Parse user input such as ``"1-3, 5, 8-"`` into a list of ranges."""
        raise NotImplementedError


@dataclass
class PdfSource:
    """An input PDF and the options that apply to it."""

    path: Path
    page_ranges: list[PageRange] = field(default_factory=list)  # empty = all pages
    reverse: bool = False  # useful for collating back-side scans

    @property
    def name(self) -> str:
        return self.path.name

    def page_count(self) -> int:
        """Return the total number of pages in the file."""
        raise NotImplementedError

    def selected_page_indices(self) -> list[int]:
        """Return 0-based page indices after applying ranges and ``reverse``."""
        raise NotImplementedError
