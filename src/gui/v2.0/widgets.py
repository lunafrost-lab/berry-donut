import tkinter as tk
from tkinter import ttk

PLACEHOLDER_COLOR = "#9a9a9a"
NORMAL_COLOR = "#000000"

def numeric_entry(parent, width=6):
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
        if P == "" or P.isdigit():
            return True
        ent.bell()
        return False

    ent.configure(validate="key", validatecommand=(ent.register(validate), "%P"))
    ent.bind("<FocusIn>", on_focus_in)
    ent.bind("<FocusOut>", on_focus_out)
    return ent, var
