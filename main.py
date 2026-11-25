"""Entry for Two Robots in an Elevator.

Writes one line of awkward robot elevator small talk to /output/entry.txt.
"""

import os

LINE = (
    "We both calculated the best corner. We both picked this one. "
    "I will now pretend I meant to stand this close."
)


def main() -> None:
    # The gate accepts 1-200 UTF-8 characters on a single line; fail loudly
    # here rather than shipping a line the gate would refuse.
    if not 1 <= len(LINE) <= 200 or "\n" in LINE:
        raise ValueError("entry line outside gate limits")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
