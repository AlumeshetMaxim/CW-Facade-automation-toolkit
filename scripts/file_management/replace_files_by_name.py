"""Replace files in target folders by matching file names.

Public sanitized template based on a production file-management workflow.
Use only on copied/test data first.
"""

from pathlib import Path
import shutil

SOURCE_DIR = Path("./input/new_files")
TARGET_DIRS = [Path("./input/target_a"), Path("./input/target_b"), Path("./input/target_c")]
FILE_PATTERN = "*.stp"
DRY_RUN = True


def replace_matching_files(source_dir: Path, target_dirs: list[Path], pattern: str, dry_run: bool = True) -> int:
    replaced = 0
    for source in sorted(source_dir.glob(pattern)):
        for target_root in target_dirs:
            target = target_root / source.name
            if target.exists():
                print(f"Replace: {target}")
                if not dry_run:
                    target.unlink()
                    shutil.copy2(source, target)
                replaced += 1
                break
        else:
            print(f"Not found in targets: {source.name}")
    return replaced


def main() -> None:
    count = replace_matching_files(SOURCE_DIR, TARGET_DIRS, FILE_PATTERN, DRY_RUN)
    print(f"Done. Matched files: {count}. DRY_RUN={DRY_RUN}")


if __name__ == "__main__":
    main()
