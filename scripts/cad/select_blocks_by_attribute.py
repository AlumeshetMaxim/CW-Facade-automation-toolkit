"""Template: find CAD block references by attribute text.

Public sanitized version. Connect to AutoCAD/BricsCAD COM locally.
"""

SEARCH_TEXTS = ["T27", "END-L-T"]
PARTIAL_MATCH = False
CASE_INSENSITIVE = True
MATCH_MODE = "ANY"


def normalize(value: str) -> str:
    value = str(value or "").strip()
    return value.lower() if CASE_INSENSITIVE else value


def value_matches(candidate: str, target: str) -> bool:
    candidate_norm = normalize(candidate)
    target_norm = normalize(target)
    return target_norm in candidate_norm if PARTIAL_MATCH else candidate_norm == target_norm


def object_matches(attribute_values: list[str], search_texts: list[str]) -> bool:
    matches = [text for text in search_texts if any(value_matches(value, text) for value in attribute_values)]
    if MATCH_MODE == "ALL":
        return len(matches) == len(search_texts)
    return bool(matches)


def main() -> None:
    sample_attributes = ["T27", "SAMPLE"]
    print("Matches:", object_matches(sample_attributes, SEARCH_TEXTS))


if __name__ == "__main__":
    main()
