"""Extract selected pages from a PDF by 1-based page numbers.

Example:
    python scripts/pdf/extract_selected_pages.py examples/input.pdf reports/selected.pdf --pages 1,3,5-8
"""

from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def parse_page_ranges(value: str) -> list[int]:
    pages: list[int] = []
    for part in value.split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            start_text, end_text = part.split('-', 1)
            start = int(start_text)
            end = int(end_text)
            if start > end:
                start, end = end, start
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    return sorted(dict.fromkeys(pages))


def extract_pages(input_pdf: Path, output_pdf: Path, pages_1_based: list[int]) -> Path:
    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()
    total = len(reader.pages)

    for page_number in pages_1_based:
        if 1 <= page_number <= total:
            writer.add_page(reader.pages[page_number - 1])
        else:
            print(f'Page out of range: {page_number}')

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    with output_pdf.open('wb') as file:
        writer.write(file)
    return output_pdf


def main() -> None:
    parser = argparse.ArgumentParser(description='Extract selected pages from a PDF.')
    parser.add_argument('input_pdf', type=Path, help='Source PDF file')
    parser.add_argument('output_pdf', type=Path, help='Output PDF file')
    parser.add_argument('--pages', required=True, help='Pages to extract, for example: 1,3,5-8')
    args = parser.parse_args()

    pages = parse_page_ranges(args.pages)
    output = extract_pages(args.input_pdf, args.output_pdf, pages)
    print(f'Created: {output}')


if __name__ == '__main__':
    main()
