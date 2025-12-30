### Berry Combination – Changelog

All notable changes to this project will be documented in this file.

## [v2.8-dev] – 30 December 2025
- **Stabilization** release. See `src/gui/current/CHANGELOG.md` for technical details.

## [v2.0] – 29 December 2025
**✨ New Features**
- **Pagination**: Query results are now limited to **50 per page** to prevent freezing on large datasets.
- **Navigation Button**s: Easily move through results with **First, Prev, Next, Last** buttons.
- `Reset` Button: Clear all filters and results, returning the app to its initial state.
- **Dynamic Export**: Export results to Excel is now available **after running a query**.

**🖌️ UI / UX Improvements**
- `Run Query` button always remains **centered below the progress bar**.
- Navigation buttons appear neatly next to `Run Query` (order: First → Prev → Next → Last).
- `Reset` / `Export` buttons appear on the **right side**, without shifting other buttons.
- Progress text now shows the current range of results per page:
  - Example: `Page 3/5 — 101-150 / 216 results`.
- Buttons automatically **enable/disable** depending on the page:
  - First & Prev disabled on first page
  - Next & Last disabled on last page
- Layout remains elegant and stable, even after resetting or navigating pages.

**🐞 Bug Fixes**
- Navigation buttons no longer remain active on the first or last page.
- Reset button now properly hides navigation and export buttons.
- Fixed issues where buttons could shift position after page navigation.

## [v1.8] – 27 December 2025
**Added**
- Menu bar with `File → Exit` and `Help → About` options showing app info and version.
- Flavor filter expanded to 5 columns (`Flavor1` to `Flavor5`) with min/max support.
- Progress bar and status text to display query status in real-time.
- Numeric entry helper with placeholder and input validation (numbers only).
- Treeview columns updated:
  - Columns `Lv+`, `Score`, `★`, and `×` adjusted for width and alignment.
  - Column sorting improved and more reliable.
- `Exclude Berry` modal enhanced:
  - `Clear` button to reset selections.
  - Scroll and mousewheel support.
- Long label text wrapped for better readability.

**Changed**
- UI more modular and organized, all panels implemented with _build_* methods.
- Query builder (build_query) supports flavor equality for up to 5 flavors simultaneously.
- Progress bar switches to indeterminate mode while running a query, back to determinate when finished.
- Treeview and detail panel updated to display selected berry combo more clearly.
- Placeholder entries for numeric fields use gray color, turning black when filled.

**Fixed**
- Fixed numeric entry validation bug (non-digit input now rejected).
- Fixed inconsistent column sorting behavior.
- Fixed issue where exclude berry window did not remain focused when opened.

## [v1.6] – 25 December 2025
- **Initial Release**
- **Filters**
  - `Flavor1 = Flavor2`, dominant over other flavors.
  - Min value input for `Flavor`, `Star`, `FlavorScore`, `LvBoost`, and `Calories`.  
    All fields define the minimal value for each category.
  - `Exclude Berry` to omit selected berries from results.

- **Buttons**
  - `Run Query`: execute filter query.
  - `Export to XLSX`: export results to Excel.

- **Process Bar**
  - Shows status: `Idle`, `Running…`, result rows count.

- **Result Display**
  - Selected BerryCombo displayed above the table.
  - Result table: sortable ascending/descending on each column.
  - Clickable rows to show BerryCombo above the table.
