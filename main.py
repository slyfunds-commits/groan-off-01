"""Groan-Off R1 entry: a one-line dad joke.

Device: P10 familiar-phrase hijack — a saying taken literally.
Writes the keeper line byte-exact to /output/entry.txt.
"""

import os

ENTRY = "I told my son to stand up for himself, and now he stands up every time someone says his name."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
