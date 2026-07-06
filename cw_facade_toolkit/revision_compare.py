"""Utilities for comparing two simplified facade schedules.

The comparison is based on public, simplified CSV/Excel data and can be used
as a starting point for drawing, fabrication or MTO revision checks.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

KEY_COLUMNS = ["unit", "item_type", "part_name"]
VALUE_COLUMNS = ["quantity"]


def _read_table(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() in {".xlsx", ".xlsm", ".xls"}:
        return pd.read_excel(path)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    raise ValueError("Unsupported file type. Use CSV or Excel.")


def compare_schedules(old_path: str | Path, new_path: str | Path) -> pd.DataFrame:
    """Compare two simplified schedules and return added, removed and changed rows."""
    old_df = _read_table(old_path).copy()
    new_df = _read_table(new_path).copy()

    required = set(KEY_COLUMNS + VALUE_COLUMNS)
    for label, df in {"old": old_df, "new": new_df}.items():
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns in {label} file: {', '.join(sorted(missing))}")

    old_df["_source_old"] = True
    new_df["_source_new"] = True

    merged = old_df.merge(
        new_df,
        on=KEY_COLUMNS,
        how="outer",
        suffixes=("_old", "_new"),
    )

    def status(row: pd.Series) -> str:
        if pd.isna(row.get("_source_old")):
            return "ADDED"
        if pd.isna(row.get("_source_new")):
            return "REMOVED"
        if row.get("quantity_old") != row.get("quantity_new"):
            return "CHANGED"
        return "UNCHANGED"

    merged["status"] = merged.apply(status, axis=1)
    result = merged[KEY_COLUMNS + ["quantity_old", "quantity_new", "status"]]
    return result.sort_values(KEY_COLUMNS).reset_index(drop=True)
