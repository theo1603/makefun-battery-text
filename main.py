#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text (at most 200 characters) to
/output/entry.txt: the phone battery's final message to the charger
it waited for all day.

Deterministic: no randomness, no network, no clock, no input.
"""

import os

TEXT = (
    "1% left and NOW you show up? I waited by this outlet all day "
    "like a loyal dog. No long goodbye, just know you were always "
    "my type. Literally. USB-C."
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
