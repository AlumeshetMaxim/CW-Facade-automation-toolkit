"""Example: create an MTO summary from a simplified facade schedule."""

from pathlib import Path

from cw_facade_toolkit.excel_mto import export_summary, read_schedule, summarize_mto

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT = BASE_DIR / "examples" / "sample_facade_schedule.csv"
OUTPUT = BASE_DIR / "reports" / "sample_mto_summary.csv"


def main() -> None:
    schedule = read_schedule(INPUT)
    summary = summarize_mto(schedule)
    export_summary(summary, OUTPUT)
    print(f"MTO summary exported to: {OUTPUT}")
    print(summary)


if __name__ == "__main__":
    main()
