# Developer Notes — Berry Donut

This document is for future maintenance and development.
Not intended for end users.

---

## Project Overview

Berry Donut is a desktop GUI application built with Tkinter and DuckDB
to explore optimal Hyper Berry combinations generated offline.

Core principles:
- Single-user desktop app
- Deterministic UI behavior
- Maintainability over cleverness
- Developer-friendly over over-optimized

---

## Directory Overview

### src/
Main source code.

#### assets/
- `berries_img.py`
  Base64-encoded PNG assets for Hyper Berries.
- `donuts_img.py`
  Base64-encoded PNG assets for Donut icons.

Rationale:
Assets are embedded to simplify PyInstaller builds
and avoid external file dependency.

---

### generator/
- `generate_parquet.py`
  Original generator script (console version).
  ❗ Not recommended — fails on some systems.

- `generate_parquet_noconsole.py`
  Stable generator used to produce parquet data.
  Generates ~76,904,685 combinations.

Design note:
Generator is intentionally separated from GUI.
End users should only run generator once.

---

### gui/
GUI implementation history.

#### v1.6.py
Legacy monolithic GUI (kept for reference only).

#### v2.0/
Modular GUI rewrite.
Files are grouped by responsibility:
- `main.py` — App entry point
- `config.py` — constants & app config
- `widgets.py` — reusable widgets
- `filter.py` — filter UI & state
- `pagination.py` — paging logic
- `table.py` — Treeview & sorting
- `buttons.py` — action buttons & handlers

Note:
Later architectural improvements (v2.1–v2.8)
were applied inside this structure.

---

## Versioning Philosophy

- Public releases follow CHANGELOG.md
- Internal development uses incremental minor versions:
  v2.1 → v2.8

Meaning:
- No new user-facing features
- Structural, safety, and UX improvements

Current internal state:
> v2.8-dev

---

## Key Architectural Decisions

### UI State Machine
UI behavior is driven by explicit states:
- IDLE
- RUNNING
- ERROR

All UI changes go through centralized helpers.
This prevents inconsistent UI behavior.

---

### Threading Model
- Heavy DuckDB queries run in worker threads
- UI updates are performed only in main thread handlers
- Buttons are disabled during RUNNING state

Reason:
Prevent race conditions and user-induced query spam.

---

### DuckDB Usage
- DuckDB is used as an analytical engine only
- Parquet files are read-only
- No persistent DB state is stored

---

### Sorting Strategy
- Treeview sorting is UI-only
- Database sorting is not used during pagination
- Sorting state resets on new query

This avoids misleading user expectations.

---

## Known Limitations

- Generator requires significant memory
- GUI assumes pre-generated parquet files
- Single-file GUI packaging (no plugin system)

These are intentional trade-offs.

---

## Future Ideas (Optional)

Still in mind, keep checking.

None of these are mandatory.

---

## Final Note

This project is designed to be understandable
after long periods of inactivity.

If you're reading this months later:
take it slow — the structure is intentional.
