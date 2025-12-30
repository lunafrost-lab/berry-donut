import sys
from pathlib import Path
import ctypes

ROOT = Path(__file__).parent.parent.parent

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and PyInstaller exe
    """
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return ROOT / relative_path

APP_VERSION = "2.8-dev"
PARQUET_PATH = "all_8berry_master_batch*.parquet"
FLAVORS = ["Sweet","Spicy","Sour","Bitter","Fresh"]

ICON_PNG = resource_path("assets/png/donuts/donut_mix05.png")
ICON_ICO = resource_path("assets/ico/donut_mix05.ico")

PLACEHOLDER_COLOR = "#9a9a9a"
NORMAL_COLOR = "#000000"

BERRY_NAMES = [
    "Hyper Cheri Berry","Hyper Chesto Berry","Hyper Pecha Berry","Hyper Rawst Berry","Hyper Aspear Berry",
    "Hyper Oran Berry","Hyper Persim Berry","Hyper Lum Berry","Hyper Sitrus Berry","Hyper Pomeg Berry",
    "Hyper Kelpsy Berry","Hyper Qualot Berry","Hyper Hondew Berry","Hyper Grepa Berry","Hyper Tamato Berry",
    "Hyper Occa Berry","Hyper Passho Berry","Hyper Wacan Berry","Hyper Rindo Berry","Hyper Yache Berry",
    "Hyper Chople Berry","Hyper Kebia Berry","Hyper Shuca Berry","Hyper Coba Berry","Hyper Payapa Berry",
    "Hyper Tanga Berry","Hyper Charti Berry","Hyper Kasib Berry","Hyper Haban Berry","Hyper Colbur Berry",
    "Hyper Babiri Berry","Hyper Chilan Berry","Hyper Roseli Berry"
]

# Windows taskbar AppUserModelID
def set_app_user_model_id():
    if hasattr(ctypes, "windll"):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "lunafrost.berrygui"
        )
