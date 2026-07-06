"""Split a PDF into files with a fixed number of pages.

Based on a real drawing-package workflow, sanitized for public use.
"""

from pathlib import Path

from cw_facade_toolkit.pdf_tools import split_pdf_by_page_groups

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_DIR = Path("./reports/split")
PAGES_PER_FILE = 3
NAME_TEMPLATE = "drawing_package_part_{index:03d}.pdf"


def main() -> None:
    outputs = split_pdf_by_page_groups(INPUT_PDF, OUTPUT_DIR, PAGES_PER_FILE, NAME_TEMPLATE)
    for output in outputs:
        print(f"Created: {output}")


if __name__ == "__main__":
    main()
