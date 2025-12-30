import tkinter as tk
from tkinter import ttk

class BerryButtons:
    def __init__(self, parent, run_callback, reset_callback, export_callback,
                 first_callback, prev_callback, next_callback, last_callback):
        self.parent = parent

        # simpan callback
        self.run_callback = run_callback
        self.reset_callback = reset_callback
        self.export_callback = export_callback
        self.first_callback = first_callback
        self.prev_callback = prev_callback
        self.next_callback = next_callback
        self.last_callback = last_callback

        # inisialisasi tombol
        self._build_buttons()

    def _build_buttons(self):
        b_frame = ttk.Frame(self.parent)
        b_frame.pack(pady=5, fill="x")

        # frame kiri (spacing)
        left_frame = ttk.Frame(b_frame)
        left_frame.pack(side="left", expand=True)

        # frame tengah → Run Query + navigasi
        center_frame = ttk.Frame(b_frame)
        center_frame.pack(side="left")

        # tombol Run Query
        self.run_btn = ttk.Button(center_frame, text="Run Query", command=self.run_callback)
        self.run_btn.pack(side="left", padx=2)

        # tombol navigasi
        self.first_btn = ttk.Button(center_frame, text="⏮ First", command=self.first_callback)
        self.prev_btn = ttk.Button(center_frame, text="⏪ Prev", command=self.prev_callback)
        self.next_btn = ttk.Button(center_frame, text="Next ⏩", command=self.next_callback)
        self.last_btn = ttk.Button(center_frame, text="Last ⏭", command=self.last_callback)

        for btn in [self.first_btn, self.prev_btn, self.next_btn, self.last_btn]:
            btn.pack_forget()  # default hidden

        # frame kanan → tombol aksi
        right_frame = ttk.Frame(b_frame)
        right_frame.pack(side="left", expand=True)

        self.reset_btn = ttk.Button(right_frame, text="Reset", command=self.reset_callback)
        self.export_btn = ttk.Button(right_frame, text="Export XLSX", command=self.export_callback)
        for btn in [self.reset_btn, self.export_btn]:
            btn.pack_forget()  # default hidden
