import tkinter as tk
from config import APP_VERSION, ICON_PNG, ICON_ICO
from filters import build_filters
from buttons import build_buttons
from table import build_table
from pagination import PaginationManager

class BerryGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"Berry Combination v{APP_VERSION}")
        self.geometry("1200x500")
        self.pagination = PaginationManager(page_size=50)
        self.iconphoto(True, tk.PhotoImage(file=str(ICON_PNG)))
        self.iconbitmap(str(ICON_ICO))

        build_filters(self)
        build_buttons(self)
        build_table(self)

if __name__ == "__main__":
    app = BerryGUI()
    app.mainloop()
