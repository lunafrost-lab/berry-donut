import tkinter as tk
from tkinter import ttk, Toplevel
from config import FLAVORS, BERRY_NAMES
from widgets import numeric_entry

def build_filters(parent, callbacks=None):
    """
    Buat frame filter lengkap.
    callbacks: dict dengan key 'open_exclude' → fungsi ketika klik select exclude
    """
    frame = ttk.LabelFrame(parent, text="Filters")
    frame.pack(fill="x", padx=10, pady=5)

    # Flavor Comboboxes
    f = ttk.Frame(frame)
    f.pack(anchor="w")
    flavor_vars = [tk.StringVar() for _ in range(5)]

    for i, var in enumerate(flavor_vars):
        ttk.Label(f, text=f"Flavor{i+1}").pack(side="left")
        ttk.Combobox(f, values=[""] + FLAVORS, textvariable=var, width=10).pack(side="left", padx=2)
        if i < 4:
            ttk.Label(f, text="=").pack(side="left")

    # Min / Max for base flavor
    ttk.Label(f, text="Min").pack(side="left", padx=2)
    fmin_ent, fmin_var = numeric_entry(f)
    fmin_ent.pack(side="left")

    ttk.Label(f, text="Max").pack(side="left", padx=2)
    fmax_ent, fmax_var = numeric_entry(f)
    fmax_ent.pack(side="left")

    # Other filters: Star, FlavorScore, LvBoost, Calories
    o = ttk.Frame(frame)
    o.pack(anchor="w", pady=2)

    star_ent, star_var = numeric_entry(o, 4)
    fs_ent, fs_var = numeric_entry(o)
    lv_ent, lv_var = numeric_entry(o)
    cal_ent, cal_var = numeric_entry(o)

    filters = {
        "flavors": flavor_vars,
        "fmin": fmin_var,
        "fmax": fmax_var,
        "star": star_var,
        "fs": fs_var,
        "lv": lv_var,
        "cal": cal_var,
    }

    # Layout
    ttk.Label(o, text="Star ≥").pack(side="left")
    star_ent.pack(side="left", padx=2)
    ttk.Label(o, text="FlavorScore ≥").pack(side="left")
    fs_ent.pack(side="left", padx=2)
    ttk.Label(o, text="LvBoost ≥").pack(side="left")
    lv_ent.pack(side="left", padx=2)
    ttk.Label(o, text="Calories ≥").pack(side="left")
    cal_ent.pack(side="left", padx=2)

    # Exclude Berry
    e = ttk.Frame(frame)
    e.pack(anchor="w", pady=2)
    ttk.Label(e, text="Exclude Berry").pack(side="left")
    exclude_btn = ttk.Button(e, text="Select", command=lambda: callbacks.get("open_exclude")() if callbacks else None)
    exclude_btn.pack(side="left", padx=5)
    exclude_label = tk.StringVar(value="None")
    ttk.Label(e, textvariable=exclude_label, wraplength=600, justify="left").pack(side="left", padx=5)

    filters.update({
        "exclude_label": exclude_label,
        "exclude_btn": exclude_btn,
    })

    return frame, filters
