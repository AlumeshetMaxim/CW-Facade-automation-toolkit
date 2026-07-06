"""Template: count selected facade block names by floor.

Use with simplified sample names or connect to a local DWG extraction routine.
"""

from collections import Counter, defaultdict

TARGET_BLOCK_NAMES = {"MULLION_A", "MULLION_B"}


def count_by_floor(rows: list[tuple[int, str]]) -> dict[int, Counter[str]]:
    result: dict[int, Counter[str]] = defaultdict(Counter)
    for floor, block_name in rows:
        if block_name in TARGET_BLOCK_NAMES:
            result[floor][block_name] += 1
    return dict(result)


def main() -> None:
    sample = [(3, "MULLION_A"), (3, "MULLION_A"), (4, "MULLION_B")]
    print(count_by_floor(sample))


if __name__ == "__main__":
    main()
