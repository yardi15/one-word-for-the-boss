#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes the entry word to /output/entry.txt. The entry is exactly one word
describing the boss.
"""

import os

ENTRY_WORD = "seagull"
OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate guard: the entry must be exactly one word, 1-30 characters,
    # and not only whitespace.
    word = ENTRY_WORD.strip()
    if not word or len(word) > 30 or len(word.split()) != 1:
        raise ValueError(
            "entry must be exactly one word of 1-30 characters, got %r" % ENTRY_WORD
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
