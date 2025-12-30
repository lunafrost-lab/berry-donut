# GUI Changelog — v2.8-dev
Stabilization Era

This changelog documents internal and technical changes made during
the v2.8 development cycle. This era focuses on stability, correctness,
and long-term maintainability rather than feature expansion.

---

## [v2.8-dev] — Stabilization Era

### Added
- Centralized UI state management (`UIState`)
- Unified `_set_ui_state()` to control buttons, progress, and status
- Query cache layer to prevent redundant database calls
- Helper methods for:
  - status updates
  - running state handling
  - pagination reset
- Developer Notes (`DEV_NOTES.md`) to document internal decisions

### Changed
- Refactored long UI handlers into smaller helper functions
- Moved repetitive reset logic into dedicated helpers
- Replaced ad-hoc button disabling with state-based control
- Improved Treeview sorting logic (UI + DB consistency)

### Fixed
- DuckDB connection leaks
- UI race conditions caused by threading callbacks
- Run button spamming during active queries
- Inconsistent UI state after query failure

### Removed
- Redundant `_set_running(False)` calls
- Direct UI mutation scattered across handlers
- Legacy error-handling paths that conflicted with UI state logic

### Notes
- This version marks the first use of `current/` vs `archive/` structure
- v2.8-dev is the reference point for future major versions
