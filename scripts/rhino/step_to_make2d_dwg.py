"""Rhino workflow template: STEP to Make2D to DWG.

Run inside Rhino. Public version uses generic folders and view names.
"""

from pathlib import Path

try:
    import rhinoscriptsyntax as rs
except ImportError:
    rs = None

STP_FOLDER = Path("./examples/stp")
OUT_FOLDER = Path("./reports/rhino_make2d")
VIEWS = ["TOP", "FRONT", "RIGHT"]


def main() -> None:
    if rs is None:
        print("Run this script inside Rhino.")
        return

    OUT_FOLDER.mkdir(parents=True, exist_ok=True)
    for step_path in sorted(STP_FOLDER.glob("*.stp")) + sorted(STP_FOLDER.glob("*.step")):
        print("Process:", step_path)
        # Local Rhino workflow can import, run Make2D for each view, and export DWG.
        # Keep project-specific paths and data outside the public repository.


if __name__ == "__main__":
    main()
