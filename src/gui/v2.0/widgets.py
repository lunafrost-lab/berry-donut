import tkinter as tk
from tkinter import ttk

def numeric_entry(parent, width=6, placeholder="0"):
    var = tk.StringVar(value=placeholder)
    ent = ttk.Entry(parent, textvariable=var, width=width, foreground="#9a9a9a")

    def on_focus_in(_):
        if var.get() == placeholder:
            var.set("")
            ent.configure(foreground="#000000")

    def on_focus_out(_):
        if var.get() == "":
            var.set(placeholder)
            ent.configure(foreground="#9a9a9a")

    def validate(P):
        if P == "" or P.isdigit():
            return True
        ent.bell()
        return False

    ent.configure(validate="key", validatecommand=(ent.register(validate), "%P"))
    ent.bind("<FocusIn>", on_focus_in)
    ent.bind("<FocusOut>", on_focus_out)
    return ent, var
