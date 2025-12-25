import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import duckdb
import pandas as pd
import threading

# =========================
# CONFIG
# =========================
PARQUET_PATH = "all_8berry_master_batch*.parquet"
FLAVORS = ["Sweet","Spicy","Sour","Bitter","Fresh"]
BERRY_NAMES = [
    "Hyper Cheri Berry","Hyper Chesto Berry","Hyper Pecha Berry","Hyper Rawst Berry","Hyper Aspear Berry",
    "Hyper Oran Berry","Hyper Persim Berry","Hyper Lum Berry","Hyper Sitrus Berry","Hyper Pomeg Berry",
    "Hyper Kelpsy Berry","Hyper Qualot Berry","Hyper Hondew Berry","Hyper Grepa Berry","Hyper Tamato Berry",
    "Hyper Occa Berry","Hyper Passho Berry","Hyper Wacan Berry","Hyper Rindo Berry","Hyper Yache Berry",
    "Hyper Chople Berry","Hyper Kebia Berry","Hyper Shuca Berry","Hyper Coba Berry","Hyper Payapa Berry",
    "Hyper Tanga Berry","Hyper Charti Berry","Hyper Kasib Berry","Hyper Haban Berry","Hyper Colbur Berry",
    "Hyper Babiri Berry","Hyper Chilan Berry","Hyper Roseli Berry"
]

# =========================
# APP
# =========================
class BerryGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Berry Combo Filter v1.5")
        self.geometry("1200x800")

        # Flavor selections
        self.flavor1_var = tk.StringVar()
        self.flavor2_var = tk.StringVar()
        self.minval_var = tk.StringVar()

        # Star / Lv / Calories / FlavorScore
        self.star_var = tk.StringVar()
        self.fs_var = tk.StringVar()
        self.lv_var = tk.StringVar()
        self.cal_var = tk.StringVar()

        # Exclude Berry
        self.exclude_list = []

        # Result dataframe
        self.df_result = None

        self._build_ui()
        self.conn = duckdb.connect()

    # =========================
    # UI
    # =========================
    def _build_ui(self):
        self._build_filter_panel()
        self._build_buttons()
        self._build_detail_panel()
        self._build_table()

    # ---------- Filter Panel ----------
    def _build_filter_panel(self):
        frame = ttk.LabelFrame(self, text="Filters")
        frame.pack(fill="x", padx=10, pady=5)

        # Flavor equality
        flavor_frame = ttk.Frame(frame)
        flavor_frame.pack(anchor="w", pady=2)

        ttk.Label(flavor_frame, text="Flavor1").pack(side="left")
        ttk.Combobox(flavor_frame, values=[""]+FLAVORS, textvariable=self.flavor1_var, width=10).pack(side="left", padx=2)
        ttk.Label(flavor_frame, text="=").pack(side="left")
        ttk.Label(flavor_frame, text="Flavor2").pack(side="left")
        ttk.Combobox(flavor_frame, values=[""]+FLAVORS, textvariable=self.flavor2_var, width=10).pack(side="left", padx=2)
        ttk.Label(flavor_frame, text="Min Value").pack(side="left", padx=5)
        ttk.Entry(flavor_frame, textvariable=self.minval_var, width=6).pack(side="left")

        # Star / FlavorScore / LvBoost / Calories
        filter_frame = ttk.Frame(frame)
        filter_frame.pack(anchor="w", pady=2)

        ttk.Label(filter_frame, text="Star").grid(row=0,column=0)
        ttk.Entry(filter_frame, textvariable=self.star_var, width=5).grid(row=0,column=1)
        ttk.Label(filter_frame, text="FlavorScore ≥").grid(row=0,column=2)
        ttk.Entry(filter_frame, textvariable=self.fs_var, width=6).grid(row=0,column=3)
        ttk.Label(filter_frame, text="LvBoost ≥").grid(row=0,column=4)
        ttk.Entry(filter_frame, textvariable=self.lv_var, width=6).grid(row=0,column=5)
        ttk.Label(filter_frame, text="Calories ≥").grid(row=0,column=6)
        ttk.Entry(filter_frame, textvariable=self.cal_var, width=6).grid(row=0,column=7)

        # Exclude Berry dropdown + checklist
        exclude_frame = ttk.Frame(frame)
        exclude_frame.pack(anchor="w", pady=2)

        ttk.Label(exclude_frame, text="Exclude Berry").pack(side="left")
        self.exclude_btn = ttk.Button(exclude_frame, text="Select Berry", command=self._open_exclude_window)
        self.exclude_btn.pack(side="left", padx=5)
        self.exclude_display_var = tk.StringVar(value="None")
        ttk.Label(exclude_frame, textvariable=self.exclude_display_var).pack(side="left", padx=10)

    def _open_exclude_window(self):
        win = Toplevel(self)
        win.title("Exclude Berry")
        win.geometry("300x400")

        lb = tk.Listbox(win, selectmode="multiple")
        lb.pack(expand=True, fill="both", padx=10, pady=10)
        for i, b in enumerate(BERRY_NAMES):
            lb.insert("end", b)
            if b in self.exclude_list:
                lb.selection_set(i)

        def save_selection():
            selected = [lb.get(i) for i in lb.curselection()]
            self.exclude_list = selected
            self.exclude_display_var.set(", ".join(selected) if selected else "None")
            win.destroy()

        ttk.Button(win, text="Save", command=save_selection).pack(pady=5)

    # ---------- Buttons ----------
    def _build_buttons(self):
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", padx=10, pady=5)
        ttk.Button(btn_frame, text="Run Query", command=self.run_query).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Export XLSX", command=self.export_xlsx).pack(side="left", padx=5)
        self.status_var = tk.StringVar(value="Idle")
        ttk.Label(btn_frame, textvariable=self.status_var).pack(side="right")

    # ---------- Detail ----------
    def _build_detail_panel(self):
        frame = ttk.LabelFrame(self, text="Selected BerryCombo")
        frame.pack(fill="x", padx=10, pady=5)
        self.detail_var = tk.StringVar(value="(Select a row)")
        ttk.Label(frame, textvariable=self.detail_var).pack(anchor="w")

    # ---------- Table ----------
    def _build_table(self):
        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        cols = ["BerryCombo","Sweet","Spicy","Sour","Bitter","Fresh","LvBoost","Calories","FlavorScore","Star","Multiplier"]

        # Scrollbars
        vsb = ttk.Scrollbar(frame, orient="vertical")
        vsb.pack(side="right", fill="y")
        hsb = ttk.Scrollbar(frame, orient="horizontal")
        hsb.pack(side="bottom", fill="x")

        self.tree = ttk.Treeview(frame, columns=cols, show="headings",
                                 yscrollcommand=vsb.set,
                                 xscrollcommand=hsb.set)
        for c in cols:
            self.tree.heading(c, text=c, command=lambda _c=c: self.sort_column(_c, False))
            self.tree.column(c, width=100)
        self.tree.pack(expand=True, fill="both")

        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    # =========================
    # Query
    # =========================
    def build_query(self):
        conditions = []

        # Flavor equality
        f1 = self.flavor1_var.get()
        f2 = self.flavor2_var.get()
        minval = self.minval_var.get()

        if f1 and f2:
            other_flavors = [f for f in FLAVORS if f not in (f1,f2)]
            conditions.append(f"{f1} = {f2}")
            conditions.append(" AND ".join([f"{f1} > {f}" for f in other_flavors]))
            if minval:
                try:
                    conditions.append(f"{f1} >= {int(minval)}")
                except ValueError:
                    pass

        # Additional filters
        if self.star_var.get():
            try: conditions.append(f"Star = {int(self.star_var.get())}")
            except ValueError: pass
        if self.fs_var.get():
            try: conditions.append(f"FlavorScore >= {int(self.fs_var.get())}")
            except ValueError: pass
        if self.lv_var.get():
            try: conditions.append(f"LvBoost >= {int(self.lv_var.get())}")
            except ValueError: pass
        if self.cal_var.get():
            try: conditions.append(f"Calories >= {int(self.cal_var.get())}")
            except ValueError: pass

        # Exclude Berry
        for b in self.exclude_list:
            conditions.append(f"BerryCombo NOT LIKE '%{b}%'")

        q = f"SELECT * FROM parquet_scan('{PARQUET_PATH}')"
        if conditions:
            q += " WHERE " + " AND ".join(conditions)
        return q

    # =========================
    # Actions
    # =========================
    def run_query(self):
        def task():
            self.status_var.set("Running...")
            try:
                df = self.conn.execute(self.build_query()).fetchdf()
                self.df_result = df
                self.tree.delete(*self.tree.get_children())
                for _, r in df.iterrows():
                    self.tree.insert("", "end", values=list(r))
                self.status_var.set(f"{len(df)} rows")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        threading.Thread(target=task, daemon=True).start()

    def export_xlsx(self):
        if self.df_result is None or self.df_result.empty: return
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                    filetypes=[("Excel","*.xlsx")])
        if file_path:
            self.df_result.to_excel(file_path, index=False)
            messagebox.showinfo("Export", f"Saved {len(self.df_result)} rows to {file_path}")

    # =========================
    # Treeview helper
    # =========================
    def sort_column(self, col, reverse):
        try:
            l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
            try:
                l.sort(key=lambda t: float(t[0]), reverse=reverse)
            except ValueError:
                l.sort(reverse=reverse)
            for index, (val, k) in enumerate(l):
                self.tree.move(k, '', index)
            self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))
        except Exception as e:
            print(e)

    def on_select(self, event):
        sel = self.tree.selection()
        if sel:
            idx = sel[0]
            combo = self.tree.item(idx)['values'][0]
            self.detail_var.set(combo)

# =========================
if __name__ == "__main__":
    app = BerryGUI()
    app.mainloop()
