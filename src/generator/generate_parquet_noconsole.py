import pandas as pd
from itertools import combinations_with_replacement
from collections import Counter
import time
import math
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys

# =============================
# DATASET BERRY
# =============================
berries = {
    "Hyper Cheri Berry":  {"Sweet":0,"Spicy":40,"Sour":0,"Bitter":0,"Fresh":0,"Lv":5,"Cal":80},
    "Hyper Chesto Berry": {"Sweet":0,"Spicy":0,"Sour":0,"Bitter":0,"Fresh":40,"Lv":3,"Cal":100},
    "Hyper Pecha Berry":  {"Sweet":40,"Spicy":0,"Sour":0,"Bitter":0,"Fresh":0,"Lv":2,"Cal":100},
    "Hyper Rawst Berry":  {"Sweet":0,"Spicy":0,"Sour":0,"Bitter":40,"Fresh":0,"Lv":3,"Cal":110},
    "Hyper Aspear Berry":{"Sweet":0,"Spicy":0,"Sour":40,"Bitter":0,"Fresh":0,"Lv":4,"Cal":90},
    "Hyper Oran Berry":   {"Sweet":10,"Spicy":20,"Sour":15,"Bitter":15,"Fresh":0,"Lv":6,"Cal":90},
    "Hyper Persim Berry": {"Sweet":0,"Spicy":15,"Sour":15,"Bitter":10,"Fresh":20,"Lv":4,"Cal":110},
    "Hyper Lum Berry":    {"Sweet":20,"Spicy":15,"Sour":10,"Bitter":0,"Fresh":15,"Lv":3,"Cal":110},
    "Hyper Sitrus Berry": {"Sweet":15,"Spicy":10,"Sour":0,"Bitter":20,"Fresh":15,"Lv":4,"Cal":120},
    "Hyper Pomeg Berry":  {"Sweet":30,"Spicy":35,"Sour":0,"Bitter":0,"Fresh":5,"Lv":7,"Cal":140},
    "Hyper Kelpsy Berry": {"Sweet":5,"Spicy":0,"Sour":0,"Bitter":30,"Fresh":35,"Lv":5,"Cal":160},
    "Hyper Qualot Berry": {"Sweet":35,"Spicy":0,"Sour":30,"Bitter":5,"Fresh":0,"Lv":4,"Cal":160},
    "Hyper Hondew Berry": {"Sweet":0,"Spicy":5,"Sour":35,"Bitter":0,"Fresh":30,"Lv":6,"Cal":150},
    "Hyper Grepa Berry":  {"Sweet":0,"Spicy":60,"Sour":25,"Bitter":0,"Fresh":5,"Lv":8,"Cal":140},
    "Hyper Tamato Berry": {"Sweet":5,"Spicy":25,"Sour":0,"Bitter":0,"Fresh":60,"Lv":6,"Cal":180},
    "Hyper Occa Berry":   {"Sweet":60,"Spicy":0,"Sour":0,"Bitter":5,"Fresh":25,"Lv":5,"Cal":180},
    "Hyper Passho Berry": {"Sweet":25,"Spicy":0,"Sour":5,"Bitter":60,"Fresh":0,"Lv":6,"Cal":200},
    "Hyper Wacan Berry":  {"Sweet":0,"Spicy":5,"Sour":60,"Bitter":25,"Fresh":0,"Lv":7,"Cal":160},
    "Hyper Rindo Berry":  {"Sweet":15,"Spicy":55,"Sour":0,"Bitter":5,"Fresh":25,"Lv":9,"Cal":210},
    "Hyper Yache Berry":  {"Sweet":25,"Spicy":0,"Sour":5,"Bitter":15,"Fresh":55,"Lv":7,"Cal":250},
    "Hyper Chople Berry": {"Sweet":55,"Spicy":5,"Sour":15,"Bitter":25,"Fresh":0,"Lv":6,"Cal":250},
    "Hyper Kebia Berry":  {"Sweet":0,"Spicy":15,"Sour":25,"Bitter":55,"Fresh":5,"Lv":7,"Cal":270},
    "Hyper Shuca Berry":  {"Sweet":5,"Spicy":25,"Sour":55,"Bitter":0,"Fresh":15,"Lv":8,"Cal":230},
    "Hyper Coba Berry":   {"Sweet":10,"Spicy":95,"Sour":0,"Bitter":10,"Fresh":5,"Lv":10,"Cal":240},
    "Hyper Payapa Berry": {"Sweet":5,"Spicy":0,"Sour":10,"Bitter":10,"Fresh":95,"Lv":8,"Cal":300},
    "Hyper Tanga Berry":  {"Sweet":95,"Spicy":10,"Sour":10,"Bitter":5,"Fresh":0,"Lv":7,"Cal":300},
    "Hyper Charti Berry": {"Sweet":0,"Spicy":10,"Sour":5,"Bitter":95,"Fresh":10,"Lv":8,"Cal":330},
    "Hyper Kasib Berry":  {"Sweet":10,"Spicy":5,"Sour":95,"Bitter":0,"Fresh":10,"Lv":9,"Cal":270},
    "Hyper Haban Berry":  {"Sweet":85,"Spicy":0,"Sour":0,"Bitter":0,"Fresh":65,"Lv":8,"Cal":370},
    "Hyper Colbur Berry": {"Sweet":0,"Spicy":0,"Sour":65,"Bitter":0,"Fresh":85,"Lv":9,"Cal":370},
    "Hyper Babiri Berry": {"Sweet":0,"Spicy":0,"Sour":65,"Bitter":85,"Fresh":0,"Lv":9,"Cal":400},
    "Hyper Chilan Berry": {"Sweet":0,"Spicy":85,"Sour":0,"Bitter":65,"Fresh":0,"Lv":9,"Cal":370},
    "Hyper Roseli Berry": {"Sweet":0,"Spicy":65,"Sour":85,"Bitter":0,"Fresh":0,"Lv":10,"Cal":340},
}

# =============================
# STAR & MULTIPLIER
# =============================
def get_star_multiplier(flavor_score):
    if flavor_score < 120: return 0, 1.0
    elif flavor_score < 240: return 1, 1.1
    elif flavor_score < 360: return 2, 1.2
    elif flavor_score < 700: return 3, 1.3
    elif flavor_score < 960: return 4, 1.4
    else: return 5, 1.5

# =============================
# GUI GENERATOR
# =============================
class GeneratorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Berry Combo Master by lunafrost-lab")
        self.geometry("500x180")
        self.resizable(False, False)

        self.status = tk.StringVar(value="Waiting to start...")
        ttk.Label(self, textvariable=self.status).pack(pady=10)

        self.progress = ttk.Progressbar(self, length=350, mode="determinate")
        self.progress.pack(pady=10)

        ttk.Button(self, text="Start Generation", command=self.start).pack(pady=10)

    def start(self):
        threading.Thread(target=self.generate, daemon=True).start()

    def generate(self):
        berry_names = list(berries.keys())
        total_combos = math.comb(len(berry_names) + 8 - 1, 8)

        batch_size = 2_000_000
        batch = []
        batch_id = 0
        processed = 0

        start_time = time.time()

        for combo in combinations_with_replacement(berry_names, 8):
            total_flavor = {k: 0 for k in ["Sweet","Spicy","Sour","Bitter","Fresh"]}
            lv = cal = 0

            for b in combo:
                for k in total_flavor:
                    total_flavor[k] += berries[b][k]
                lv += berries[b]["Lv"]
                cal += berries[b]["Cal"]

            flavor_score = sum(total_flavor.values())
            star, mul = get_star_multiplier(flavor_score)
            lv = round(lv * mul)
            cal = round(cal * mul)

            combo_str = ", ".join(f"{b} x{c}" for b,c in Counter(combo).items())

            batch.append({
                "BerryCombo": combo_str,
                **total_flavor,
                "LvBoost": lv,
                "Calories": cal,
                "FlavorScore": flavor_score,
                "Star": star,
                "Multiplier": mul
            })

            processed += 1

            if len(batch) >= batch_size:
                pd.DataFrame(batch).to_parquet(f"all_8berry_master_batch{batch_id}.parquet", index=False)
                batch.clear()
                batch_id += 1

            if processed % 10_000 == 0:
                pct = processed / total_combos * 100
                self.progress["value"] = pct
                self.status.set(f"Processing: {processed:,} / {total_combos:,}")
                self.update_idletasks()

        if batch:
            pd.DataFrame(batch).to_parquet(f"all_8berry_master_batch{batch_id}.parquet", index=False)

        self.progress["value"] = 100
        self.status.set("Generation finished")
        messagebox.showinfo("Done", "All parquet files generated successfully.")

# =============================
if __name__ == "__main__":
    GeneratorGUI().mainloop()
