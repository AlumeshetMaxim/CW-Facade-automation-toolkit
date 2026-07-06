"""PDF to JPEG workflow notes.

This public placeholder documents the conversion workflow. Add your preferred
local PDF rendering backend when running on your machine.
"""

INPUT_PDF = "./examples/input.pdf"
OUTPUT_DIR = "./reports/jpeg_pages"
DPI = 300


def main() -> None:
    print("Input:", INPUT_PDF)
    print("Output:", OUTPUT_DIR)
    print("DPI:", DPI)


if __name__ == "__main__":
    main()
