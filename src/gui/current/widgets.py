import tkinter as tk
from tkinter import ttk
from config import PLACEHOLDER_COLOR, NORMAL_COLOR

def numeric_entry(parent, width=6):
    """
    Buat ttk.Entry untuk angka dengan placeholder 0
    """
    var = tk.StringVar(value="0")
    ent = ttk.Entry(parent, textvariable=var, width=width, foreground=PLACEHOLDER_COLOR)

    def on_focus_in(_):
        if var.get() == "0":
            var.set("")
            ent.configure(foreground=NORMAL_COLOR)

    def on_focus_out(_):
        if var.get() == "":
            var.set("0")
            ent.configure(foreground=PLACEHOLDER_COLOR)

    def validate(P):
        if P == "":
            return True
        if P.isdigit():
            return True
        ent.bell()
        return False

    ent.configure(validate="key", validatecommand=(ent.register(validate), "%P"))
    ent.bind("<FocusIn>", on_focus_in)
    ent.bind("<FocusOut>", on_focus_out)
    return ent, var


def build_progress(parent):
    """
    Frame progress + label
    """
    frame = ttk.Frame(parent)
    frame.pack(pady=5)

    progress_text = tk.StringVar(value="Waiting for query")
    ttk.Label(frame, textvariable=progress_text).pack()

    progress = ttk.Progressbar(frame, mode="determinate", length=420)
    progress.pack()
    return frame, progress, progress_text


def build_detail(parent):
    """
    Frame untuk selected BerryCombo
    """
    f = ttk.LabelFrame(parent, text="Selected BerryCombo")
    f.pack(fill="x", padx=10)

    detail_var = tk.StringVar(value="(Select a row)")
    ttk.Label(f, textvariable=detail_var).pack(anchor="w")
    return f, detail_var
