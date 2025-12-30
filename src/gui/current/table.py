import tkinter as tk
from tkinter import ttk

class BerryTable:
    def __init__(self, parent, on_select_callback=None):
        self.parent = parent
        self.on_select_callback = on_select_callback
        self.tree = None
        self._build_table()

    def _build_table(self):
        frame = ttk.Frame(self.parent)
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        cols = ["BerryCombo","Sweet","Spicy","Sour","Bitter","Fresh",
                "Lv+","Calories","Score","★","×"]

        vsb = ttk.Scrollbar(frame, orient="vertical")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")

        self.tree = ttk.Treeview(
            frame,
            columns=cols,
            show="headings",
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
        )

        for c in cols:
            self.tree.heading(c, text=c, command=lambda col=c: self._sort(col, False))
            if c == "BerryCombo":
                self.tree.column(c, width=420, anchor="w")
            elif c in ("Sweet","Spicy","Sour","Bitter","Fresh"):
                self.tree.column(c, width=70, anchor="center")
            elif c == "Lv+":
                self.tree.column(c, width=55, anchor="center")
            elif c == "★":
                self.tree.column(c, width=45, anchor="center")
            elif c == "Calories":
                self.tree.column(c, width=80, anchor="center")
            elif c == "×":
                self.tree.column(c, width=55, anchor="center")
            else:
                self.tree.column(c, width=80, anchor="center")

        self.tree.pack(fill="both", expand=True)

        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    def _sort(self, col, rev):
        data = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        try:
            data.sort(key=lambda t: float(t[0]), reverse=rev)
        except:
            data.sort(reverse=rev)
        for i, (_, k) in enumerate(data):
            self.tree.move(k, "", i)
        self.tree.heading(col, command=lambda: self._sort(col, not rev))

    def _on_select(self, _):
        sel = self.tree.selection()
        if sel and self.on_select_callback:
            self.on_select_callback(self.tree.item(sel[0])["values"][0])
