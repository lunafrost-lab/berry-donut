from tkinter import ttk
from widgets import numeric_entry
from config import FLAVORS, BERRY_NAMES

def build_filters(self):
    frame = ttk.LabelFrame(self, text="Filters")
    frame.pack(fill="x", padx=10, pady=5)

    f = ttk.Frame(frame)
    f.pack(anchor="w")
    self.flavor_vars = [tk.StringVar() for _ in range(5)]
    for i, var in enumerate(self.flavor_vars):
        ttk.Label(f, text=f"Flavor{i+1}").pack(side="left")
        ttk.Combobox(f, values=[""] + FLAVORS, textvariable=var, width=10).pack(side="left", padx=2)
        if i < 4: ttk.Label(f, text="=").pack(side="left")

    ttk.Label(f, text="Min").pack(side="left", padx=5)
    self.fmin_ent, self.fmin = numeric_entry(f)
    self.fmin_ent.pack(side="left")
    ttk.Label(f, text="Max").pack(side="left", padx=5)
    self.fmax_ent, self.fmax = numeric_entry(f)
    self.fmax_ent.pack(side="left")

    o = ttk.Frame(frame)
    o.pack(anchor="w", pady=2)
    ttk.Label(o, text="Star ≥").pack(side="left")
    self.star_ent, self.star = numeric_entry(o, 4); self.star_ent.pack(side="left", padx=2)
    ttk.Label(o, text="FlavorScore ≥").pack(side="left")
    self.fs_ent, self.fs = numeric_entry(o); self.fs_ent.pack(side="left", padx=2)
    ttk.Label(o, text="LvBoost ≥").pack(side="left")
    self.lv_ent, self.lv = numeric_entry(o); self.lv_ent.pack(side="left", padx=2)
    ttk.Label(o, text="Calories ≥").pack(side="left")
    self.cal_ent, self.cal = numeric_entry(o); self.cal_ent.pack(side="left", padx=2)

    e = ttk.Frame(frame)
    e.pack(anchor="w", pady=2)
    ttk.Label(e, text="Exclude Berry").pack(side="left")
    ttk.Button(e, text="Select", command=self._open_exclude).pack(side="left", padx=5)
    self.exclude_label = tk.StringVar(value="None")
    ttk.Label(e, textvariable=self.exclude_label, wraplength=600, justify="left").pack(side="left", padx=5)
