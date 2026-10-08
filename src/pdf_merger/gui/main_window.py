"""The application's main window."""

import tkinter as tk
from tkinter import ttk

from pdf_merger import __version__
from pdf_merger.core.models import MergeMode
from pdf_merger.gui.widgets import FileListFrame


class MainWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title(f"PDF Merger {__version__}")
        root.minsize(640, 420)

        self.mode = tk.StringVar(value=MergeMode.COMBINE.value)
        self.output_path = tk.StringVar()
        self.status = tk.StringVar(value="Add PDF files to begin.")

        self._build()

    def _build(self) -> None:
        main = ttk.Frame(self.root, padding=12)
        main.pack(fill="both", expand=True)
        main.columnconfigure(0, weight=1)
        main.rowconfigure(0, weight=1)

        # Input files
        files_group = ttk.LabelFrame(main, text="Input files", padding=8)
        files_group.grid(row=0, column=0, sticky="nsew")
        self.file_list = FileListFrame(files_group)
        self.file_list.pack(fill="both", expand=True)

        # Mode
        mode_group = ttk.LabelFrame(main, text="Mode", padding=8)
        mode_group.grid(row=1, column=0, sticky="ew", pady=(8, 0))
        ttk.Radiobutton(
            mode_group, text="Combine (append files in order)",
            variable=self.mode, value=MergeMode.COMBINE.value,
        ).pack(anchor="w")
        ttk.Radiobutton(
            mode_group, text="Collate (interleave pages)",
            variable=self.mode, value=MergeMode.COLLATE.value,
        ).pack(anchor="w")

        # Output
        output_group = ttk.LabelFrame(main, text="Output file", padding=8)
        output_group.grid(row=2, column=0, sticky="ew", pady=(8, 0))
        output_group.columnconfigure(0, weight=1)
        ttk.Entry(output_group, textvariable=self.output_path).grid(
            row=0, column=0, sticky="ew"
        )
        ttk.Button(output_group, text="Browse...", command=self.choose_output).grid(
            row=0, column=1, padx=(8, 0)
        )

        # Actions
        actions = ttk.Frame(main)
        actions.grid(row=3, column=0, sticky="ew", pady=(12, 0))
        ttk.Label(actions, textvariable=self.status).pack(side="left")
        ttk.Button(actions, text="Exit", command=self.root.destroy).pack(side="right")
        ttk.Button(actions, text="Run", command=self.run).pack(side="right", padx=(0, 8))

    def choose_output(self) -> None:
        """Prompt for the output file path."""
        raise NotImplementedError

    def run(self) -> None:
        """Validate inputs and run the selected merge mode."""
        raise NotImplementedError
