import pandas as pd
from itertools import combinations_with_replacement
from collections import Counter
import time
import math

# =============================
# Dataset Berry
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
# Helper Stars & Multipliers
# =============================
def get_star_multiplier(flavor_score):
    if flavor_score < 120: return 0, 1.0
    elif flavor_score < 240: return 1, 1.1
    elif flavor_score < 360: return 2, 1.2
    elif flavor_score < 700: return 3, 1.3
    elif flavor_score < 960: return 4, 1.4
    else: return 5, 1.5

# =============================
# Batch generate 2 Juta Kombinasi
# =============================
berry_names = list(berries.keys())
batch_size = 2_000_000
all_combos = combinations_with_replacement(berry_names, 8)
batch_data = []
batch_count = 0
total_count = 0
start_time = time.time()

def sec_to_hms(sec):
    h = int(sec//3600)
    m = int((sec%3600)//60)
    s = int(sec%60)
    return f"{h}h {m}m {s}s"

for combo in all_combos:
    # Hitung total flavor
    total_flavor = {k:0 for k in ["Sweet","Spicy","Sour","Bitter","Fresh"]}
    total_lv = 0
    total_cal = 0
    for b in combo:
        for k in total_flavor:
            total_flavor[k] += berries[b][k]
        total_lv += berries[b]["Lv"]
        total_cal += berries[b]["Cal"]
    
    flavor_score = sum(total_flavor.values())
    star, multiplier = get_star_multiplier(flavor_score)
    total_lv = round(total_lv * multiplier)
    total_cal = round(total_cal * multiplier)
    
    combo_str = ", ".join([f"{b} x{cnt}" for b,cnt in Counter(combo).items()])
    
    row = {
        "BerryCombo": combo_str,
        **total_flavor,
        "LvBoost": total_lv,
        "Calories": total_cal,
        "FlavorScore": flavor_score,
        "Star": star,
        "Multiplier": multiplier
    }
    batch_data.append(row)
    total_count += 1
    
    # Tulis batch
    if len(batch_data) >= batch_size:
        df = pd.DataFrame(batch_data)
        df.to_parquet(f"all_8berry_master_batch{batch_count}.parquet", index=False)
        batch_data = []
        batch_count += 1
        elapsed = time.time() - start_time
        eta_sec = elapsed / total_count * (78_000_000 - total_count)
        print(f"Batch {batch_count} selesai ({total_count} kombinasi), waktu berlalu: {sec_to_hms(elapsed)}, ETA: {sec_to_hms(eta_sec)}")

# Tulis sisa batch terakhir
if batch_data:
    df = pd.DataFrame(batch_data)
    df.to_parquet(f"all_8berry_master_batch{batch_count}.parquet", index=False)

print("File master selesai dibuat: all_8berry_master_batch*.parquet")
