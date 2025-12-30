import sys
import tkinter as tk
import ctypes
from pathlib import Path

# =========================
# CONFIG
# =========================
ROOT = Path(__file__).parent

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return ROOT / relative_path

# Versi aplikasi
APP_VERSION = "2.8-dev"

# =========================
# IMPORT MODUL GUI
# =========================
from widgets import Widgets
from table import BerryTable
from buttons import ActionButtons
from filter import Filters
from pagination import Pagination

# =========================
# APP CLASS
# =========================
class BerryGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # Windows taskbar AppUserModelID
        if hasattr(ctypes, "windll"):
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                "lunafrost.berrygui"
            )

        self.title("Berry Combination by lunafrost-lab")
        self.geometry("1200x500")

        # Hub modul
        self.widgets = Widgets(self)
        self.filters = Filters(self)
        self.table = BerryTable(self)
        self.buttons = ActionButtons(self)
        self.pagination = Pagination(self)

        # Panggil semua build UI
        self.widgets.build_all()
        self.filters.build_filters()
        self.table.build_table()
        self.buttons.build_buttons()
        self.pagination.update_buttons()

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app = BerryGUI()
    app.mainloop()
