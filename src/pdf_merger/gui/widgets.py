"""Reusable tkinter widgets."""

import tkinter as tk
from tkinter import ttk

from pdf_merger.core.models import PdfSource


class FileListFrame(ttk.Frame):
    """An ordered list of input PDFs with add/remove/reorder buttons."""

    def __init__(self, master: tk.Misc, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.sources: list[PdfSource] = []

        self.tree = ttk.Treeview(
            self, columns=("name", "pages", "range"), show="headings", height=10
        )
        self.tree.heading("name", text="File")
        self.tree.heading("pages", text="Pages")
        self.tree.heading("range", text="Range")
        self.tree.column("pages", width=60, anchor="center")
        self.tree.column("range", width=100)
        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        buttons = ttk.Frame(self)
        buttons.grid(row=0, column=2, sticky="n", padx=(8, 0))
        for text, command in (
            ("Add...", self.add_files),
            ("Remove", self.remove_selected),
            ("Move Up", self.move_up),
            ("Move Down", self.move_down),
            ("Clear", self.clear),
        ):
            ttk.Button(buttons, text=text, command=command).pack(fill="x", pady=2)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def add_files(self) -> None:
        """Prompt for PDF files and append them to the list."""
        raise NotImplementedError

    def remove_selected(self) -> None:
        raise NotImplementedError

    def move_up(self) -> None:
        raise NotImplementedError

    def move_down(self) -> None:
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError

    def refresh(self) -> None:
        """Redraw the tree from ``self.sources``."""
        raise NotImplementedError
