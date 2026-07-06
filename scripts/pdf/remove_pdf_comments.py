"""Remove comments/annotations from a PDF drawing package."""

from pathlib import Path

from cw_facade_toolkit.pdf_tools import remove_pdf_annotations

INPUT_PDF = Path("./examples/input_with_comments.pdf")
OUTPUT_PDF = Path("./reports/input_without_comments.pdf")


def main() -> None:
    output = remove_pdf_annotations(INPUT_PDF, OUTPUT_PDF)
    print(f"Created: {output}")


if __name__ == "__main__":
    main()
