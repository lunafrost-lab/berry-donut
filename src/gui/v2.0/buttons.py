from tkinter import ttk
from tkinter import filedialog
import threading
import pandas as pd

def build_buttons(self):
    frame = ttk.Frame(self)
    frame.pack(pady=5)

    self.run_btn = ttk.Button(frame, text="Run Query", command=self.run_new_query)
    self.run_btn.pack(side="left", padx=5)
    self.export_btn = ttk.Button(frame, text="Export XLSX", command=self.export_xlsx)
    self.reset_btn = ttk.Button(frame, text="Reset", command=self.reset_filters)
    self.first_btn = ttk.Button(frame, text="⏮ First", command=self.first_page)
    self.prev_btn = ttk.Button(frame, text="⏪ Prev", command=self.prev_page)
    self.next_btn = ttk.Button(frame, text="Next ⏩", command=self.next_page)
    self.last_btn = ttk.Button(frame, text="Last ⏭", command=self.last_page)

    for b in [self.export_btn, self.reset_btn, self.first_btn, self.prev_btn, self.next_btn, self.last_btn]:
        b.pack_forget()
