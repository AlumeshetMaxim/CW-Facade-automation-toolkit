"""Extract PDF pages that contain selected element/drawing codes."""

from pathlib import Path
import re

import fitz

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_PDF = Path("./reports/pages_by_codes.pdf")
CODES = ["CH1", "C25", "L22"]


def build_regex(tokens: list[str]) -> re.Pattern[str]:
    escaped = [re.escape(token) for token in tokens]
    return re.compile(r"(?<![A-Z0-9])(" + "|".join(escaped) + r")(?![A-Z0-9])", re.IGNORECASE)


def extract_pages_by_codes(input_pdf: Path, output_pdf: Path, codes: list[str]) -> list[int]:
    pattern = build_regex(codes)
    source = fitz.open(str(input_pdf))
    target = fitz.open()
    matched_pages: list[int] = []

    for index in range(source.page_count):
        text = source.load_page(index).get_text("text") or ""
        if pattern.search(text):
            target.insert_pdf(source, from_page=index, to_page=index)
            matched_pages.append(index + 1)

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    if matched_pages:
        target.save(str(output_pdf))
    target.close()
    source.close()
    return matched_pages


def main() -> None:
    matched = extract_pages_by_codes(INPUT_PDF, OUTPUT_PDF, CODES)
    print("Matched pages:", matched)
    print("Output:", OUTPUT_PDF)


if __name__ == "__main__":
    main()
