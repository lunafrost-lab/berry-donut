def build_pagination(parent, tree, reset_btn, export_btn, page_size=50):
    """
    Buat state & tombol pagination.
    Return dict state + fungsi navigasi
    """
    state = {
        "current_page": 1,
        "total_rows": 0,
        "total_pages": 1,
        "page_size": page_size,
    }

    # Tombol navigasi
    first_btn = parent.nametowidget(parent.tk.call("ttk::button", "first")) if parent.tk.call("info", "exists", "first") else None
    prev_btn = parent.nametowidget(parent.tk.call("ttk::button", "prev")) if parent.tk.call("info", "exists", "prev") else None
    next_btn = parent.nametowidget(parent.tk.call("ttk::button", "next")) if parent.tk.call("info", "exists", "next") else None
    last_btn = parent.nametowidget(parent.tk.call("ttk::button", "last")) if parent.tk.call("info", "exists", "last") else None

    buttons = {
        "first": first_btn,
        "prev": prev_btn,
        "next": next_btn,
        "last": last_btn,
        "reset": reset_btn,
        "export": export_btn,
    }

    def update_buttons():
        # Hide semua tombol navigasi default
        for btn in [buttons["first"], buttons["prev"], buttons["next"], buttons["last"]]:
            if btn:
                btn.pack_forget()

        # Tombol navigasi
        if state["total_rows"] > state["page_size"]:
            for btn in [buttons["first"], buttons["prev"], buttons["next"], buttons["last"]]:
                if btn and not btn.winfo_ismapped():
                    btn.pack(side="left", padx=2)
        else:
            for btn in [buttons["first"], buttons["prev"], buttons["next"], buttons["last"]]:
                if btn:
                    btn.pack_forget()

        # Tombol aksi
        if state["total_rows"] > 0:
