"""Template for rendering PDF drawing pages to image files.

This public template keeps only the configuration and workflow notes. Add the
renderer used in your local CAD/PDF environment, for example pypdfium2 or another
approved PDF renderer.
"""

from pathlib import Path

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_DIR = Path("./reports/rendered_pages")
DPI = 300


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Input PDF:", INPUT_PDF)
    print("Output folder:", OUTPUT_DIR)
    print("DPI:", DPI)
    print("Add your local PDF rendering backend here.")


if __name__ == "__main__":
    main()
