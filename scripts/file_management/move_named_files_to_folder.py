"""Move selected files into a target subfolder by exact file name.

Use this template for organizing STEP/STP or production files. Public version uses generic names.
"""

from pathlib import Path
import shutil

SOURCE_FOLDER = Path("./input/files")
TARGET_FOLDER = SOURCE_FOLDER / "SELECTED"
FILES_TO_MOVE = ["PART_A.stp", "PART_B.stp", "PART_C.stp"]
DRY_RUN = True


def main() -> None:
    TARGET_FOLDER.mkdir(parents=True, exist_ok=True)
    existing = {path.name.lower(): path for path in SOURCE_FOLDER.iterdir() if path.is_file()}

    for file_name in FILES_TO_MOVE:
        source = existing.get(file_name.lower())
        if source is None:
            print(f"NOT FOUND - {file_name}")
            continue
        destination = TARGET_FOLDER / source.name
        print(f"MOVE - {source.name} -> {destination}")
        if not DRY_RUN:
            shutil.move(str(source), str(destination))

    print("Done. DRY_RUN=", DRY_RUN)


if __name__ == "__main__":
    main()
