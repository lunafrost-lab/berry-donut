from tkinter import ttk

def build_table(self):
    frame = ttk.Frame(self)
    frame.pack(fill="both", expand=True, padx=10, pady=5)

    cols = ["BerryCombo","Sweet","Spicy","Sour","Bitter","Fresh","Lv+","Calories","Score","★","×"]
    self.tree = ttk.Treeview(frame, columns=cols, show="headings")
    for c in cols:
        self.tree.heading(c, text=c)
        self.tree.column(c, width=80, anchor="center")
        if c == "BerryCombo": self.tree.column(c, width=420, anchor="w")
    self.tree.pack(fill="both", expand=True)
    self.tree.bind("<<TreeviewSelect>>", self._on_select)
