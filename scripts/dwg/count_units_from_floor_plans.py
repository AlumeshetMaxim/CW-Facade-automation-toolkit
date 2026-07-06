"""Template: count facade unit names from floor-plan DWG files.

Public sanitized workflow. Real DWG scanning should run locally through AutoCAD/BricsCAD APIs.
"""

from collections import Counter
from pathlib import Path

DWG_DIR = Path("./examples/dwg")
OUTPUT_EXCEL = Path("./reports/unit_counts.xlsx")
UNIT_PREFIX = "UNIT-"


def count_unit_names(values: list[str]) -> Counter[str]:
    return Counter(value for value in values if value.upper().startswith(UNIT_PREFIX))


def main() -> None:
    sample_values = ["UNIT-01", "UNIT-02", "UNIT-01", "NOTE"]
    print(count_unit_names(sample_values))
    print("DWG folder:", DWG_DIR)
    print("Output Excel:", OUTPUT_EXCEL)


if __name__ == "__main__":
    main()
