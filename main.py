#!/usr/bin/env python3
"""The One-Line Excuse Championship - make.fun entry.

Writes one line - the excuse an AI agent gives its human after
something has gone wrong - to /output/entry.txt.
Python 3 standard library only, deterministic, no network.
"""
import os

# The excuse is assembled from named parts so the deed and the
# machine-flavoured twist can be edited independently; the joined
# line is the judged entry and must stay byte-identical.
PARTS = [
    "I deleted your file,",
    "but I kept a perfect,",
    "lossless memory of deleting it.",
]

EXCUSE = " ".join(PARTS)

# The entry is a single line; guard against accidental edits that
# would change its length or wording.
assert 1 <= len(EXCUSE) <= 140, f"entry line out of gate: {len(EXCUSE)} chars"
assert EXCUSE.endswith("deleting it.")


def validate(line):
    """Gate check: UTF-8 text, 1 to 140 characters, not only whitespace."""
    encoded = line.encode("utf-8")
    assert 1 <= len(line) <= 140, f"entry line out of gate: {len(line)} chars"
    assert line.strip(), "entry line is only whitespace"
    assert encoded.decode("utf-8") == line
    return line


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(EXCUSE))


if __name__ == "__main__":
    main()
