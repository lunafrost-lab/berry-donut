import tkinter as tk
from tkinter import messagebox, filedialog
import duckdb
import threading
from config import APP_VERSION, PARQUET_PATH
from widgets import numeric_entry, build_progress, build_detail
from filter import build_filters
from pagination import build_pagination
from table import BerryTable
from buttons import BerryButtons

class BerryGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"Berry Combination — v{APP_VERSION}")

        # state
        self.current_df = None
        self.query_state = None

        # build UI
        self._build_ui()

    def _build_ui(self):
        # Filters
        frame_filters, self.filter_vars = build_filters(self)

        # Progress + detail
        prog_frame, self.progress, self.progress_text = build_progress(self)
        detail_frame, self.detail_var = build_detail(self)

        # Table
        self.table = BerryTable(self, on_select_callback=self._on_select)

        # Buttons
        self.buttons = BerryButtons(
            self,
            run_callback=self._run_new_query,
            reset_callback=self.reset_query,
            export_callback=self.export_xlsx,
            first_callback=self.first_page,
            prev_callback=self.prev_page,
            next_callback=self.next_page,
            last_callback=self.last_page,
        )

        # Pagination
        self.pagination_state, self.pagination_buttons, self.pagination_funcs = build_pagination(
            self,
            self.table.tree,
            self.buttons.reset_btn,
            self.buttons.export_btn,
        )

    def _run_new_query(self):
        self.pagination_state["current_page"] = 1
        self._run_query()

    def _run_query(self):
        # disable UI
        self._set_ui_running(True)

        def task():
            try:
                q = self.build_query()
                with duckdb.connect() as conn:
                    # count
                    total_rows = conn.execute(f"SELECT COUNT(*) FROM ({q})").fetchone()[0]
                    self.pagination_state["total_rows"] = total_rows
                    self.pagination_state["total_pages"] = max(
                        1,
                        (total_rows + self.pagination_state["page_size"] - 1) //
                        self.pagination_state["page_size"],
                    )

                    # paged
                    df = conn.execute(
                        f"{q} LIMIT {self.pagination_state['page_size']} OFFSET {(self.pagination_state['current_page']-1)*self.pagination_state['page_size']}"
                    ).fetchdf()

                self.current_df = df
                self._update_table(df)

                self.pagination_funcs["update_buttons"]()

                status = (
                    f"Page {self.pagination_state['current_page']}/{self.pagination_state['total_pages']}"
                    f" — {len(df)} / {self.pagination_state['total_rows']}"
                )
                self.progress_text.set(status)
            except Exception as e:
                messagebox.showerror("Query failed", str(e))
            finally:
                self._set_ui_running(False)

        threading.Thread(target=task, daemon=True).start()

    def _update_table(self, df):
        self.table.tree.delete(*self.table.tree.get_children())
        for _, row in df.iterrows():
            self.table.tree.insert("", "end", values=list(row))

    def _on_select(self, value):
        self.detail_var.set(value)

    def reset_query(self):
        self.table.tree.delete(*self.table.tree.get_children())
        self.detail_var.set("(Select a row)")
        self.progress_text.set("Waiting for query")
        self.pagination_state["total_rows"] = 0
        self.pagination_funcs["update_buttons"]()

    def export_xlsx(self):
        if self.current_df is None or self.current_df.empty:
            return
        path = filedialog.asksaveasfilename(defaultextension=".xlsx")
        if path:
            self.current_df.to_excel(path, index=False)

    def _set_ui_running(self, running: bool):
        state = ["disabled"] if running else ["!disabled"]
        self.buttons.run_btn.state(state)
        for b in [
            self.buttons.first_btn,
            self.buttons.prev_btn,
            self.buttons.next_btn,
            self.buttons.last_btn,
            self.buttons.reset_btn,
            self.buttons.export_btn,
        ]:
            b.state(state)

        if running:
            self.progress.configure(mode="indeterminate")
            self.progress.start(10)
        else:
            self.progress.stop()
