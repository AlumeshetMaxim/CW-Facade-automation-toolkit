"""Reusable PDF helper functions for facade drawing packages.

These helpers are intentionally generic and do not contain project-specific paths.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:  # pragma: no cover - compatibility fallback
    from PyPDF2 import PdfReader, PdfWriter


def split_pdf_by_page_groups(
    input_pdf: str | Path,
    output_dir: str | Path,
    pages_per_file: int,
    name_template: str = "part_{index:03d}.pdf",
) -> list[Path]:
    """Split one PDF into multiple PDFs with a fixed number of pages per file."""
    if pages_per_file <= 0:
        raise ValueError("pages_per_file must be greater than zero")

    input_pdf = Path(input_pdf)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(input_pdf))
    outputs: list[Path] = []

    for file_index, start in enumerate(range(0, len(reader.pages), pages_per_file), start=1):
        writer = PdfWriter()
        end = min(start + pages_per_file, len(reader.pages))
        for page_index in range(start, end):
            writer.add_page(reader.pages[page_index])

        output_path = output_dir / name_template.format(index=file_index, start=start + 1, end=end)
        with output_path.open("wb") as file:
            writer.write(file)
        outputs.append(output_path)

    return outputs


def split_pdf_to_single_pages(input_pdf: str | Path, output_dir: str | Path, prefix: str = "page") -> list[Path]:
    """Split a PDF into one file per page."""
    return split_pdf_by_page_groups(
        input_pdf=input_pdf,
        output_dir=output_dir,
        pages_per_file=1,
        name_template=f"{prefix}_{{index:03d}}.pdf",
    )


def merge_pdfs(pdf_files: Iterable[str | Path], output_pdf: str | Path) -> Path:
    """Merge PDF files in the provided order."""
    output_pdf = Path(output_pdf)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(str(pdf_file))
        for page in reader.pages:
            writer.add_page(page)

    with output_pdf.open("wb") as file:
        writer.write(file)
    return output_pdf


def merge_first_pages(pdf_files: Iterable[str | Path], output_pdf: str | Path) -> Path:
    """Merge only the first page from each PDF file."""
    output_pdf = Path(output_pdf)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(str(pdf_file))
        if reader.pages:
            writer.add_page(reader.pages[0])

    with output_pdf.open("wb") as file:
        writer.write(file)
    return output_pdf


def remove_pdf_annotations(input_pdf: str | Path, output_pdf: str | Path) -> Path:
    """Remove page annotations/comments from a PDF."""
    input_pdf = Path(input_pdf)
    output_pdf = Path(output_pdf)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()

    for page in reader.pages:
        if "/Annots" in page:
            page.pop("/Annots", None)
        writer.add_page(page)

    with output_pdf.open("wb") as file:
        writer.write(file)
    return output_pdf


def files_from_quantity_table(base_dir: str | Path, items: Sequence[tuple[int, str]], suffix: str = ".pdf") -> list[Path]:
    """Expand a quantity/id table into an ordered list of PDF paths.

    Example: [(2, "A"), (1, "B")] becomes [A.pdf, A.pdf, B.pdf].
    """
    base_dir = Path(base_dir)
    result: list[Path] = []
    for quantity, file_id in items:
        result.extend([base_dir / f"{file_id}{suffix}" for _ in range(int(quantity))])
    return result
