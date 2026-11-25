"""Two Robots in an Elevator — v2 entry.

Prints one awkward robot small-talk line into /output/entry.txt.
The contest gate wants 1-200 UTF-8 characters on a single line.
"""

from pathlib import Path

ENTRY_LINE = (
    "I shifted my weight so the elevator would not think we were arguing. "
    "It has not thanked me."
)

OUTPUT_PATH = Path("/output/entry.txt")


def check_line(line: str) -> str:
    if "\n" in line or "\r" in line:
        raise ValueError("entry must stay on one line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > 200:
        raise ValueError("entry is longer than the 200 character gate")
    return line


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(check_line(ENTRY_LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
