"""Merge the first page from each floor-plan PDF into one package."""

from pathlib import Path

from cw_facade_toolkit.pdf_tools import merge_first_pages

BASE_DIR = Path("./examples/floor_plan_pdfs")
OUTPUT_PDF = Path("./reports/merged_first_pages.pdf")
FLOORS = range(3, 35)
NAME_TEMPLATE = "FLOOR_PLAN_{floor:02d}.pdf"


def main() -> None:
    pdf_files = [BASE_DIR / NAME_TEMPLATE.format(floor=floor) for floor in FLOORS]
    existing_files = [path for path in pdf_files if path.exists()]
    if not existing_files:
        raise FileNotFoundError(f"No input PDFs found in {BASE_DIR}")
    output = merge_first_pages(existing_files, OUTPUT_PDF)
    print(f"Created: {output}")


if __name__ == "__main__":
    main()
