"""Workflow template: batch-publish DWG files to PDF and merge the result.

Local implementation should connect to AutoCAD or BricsCAD, open each DWG,
publish layouts, then use `cw_facade_toolkit.pdf_tools.merge_pdfs`.
"""

from pathlib import Path

DWG_DIR = Path("./examples/dwg")
PDF_DIR = Path("./reports/pdf")
MERGED_PDF = Path("./reports/merged_drawing_package.pdf")


def main() -> None:
    print("DWG folder:", DWG_DIR)
    print("PDF output folder:", PDF_DIR)
    print("Merged PDF:", MERGED_PDF)
    print("Connect this template to your CAD publishing backend locally.")


if __name__ == "__main__":
    main()
