#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — a make.fun haiku entry.

Writes one haiku about debugging to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR if set, else /output, else beside this file).
Pure standard library: the grader's python3.13 image ships no
third-party packages, so this program needs none.
"""

import os
import sys

HAIKU = (
    "I set a breakpoint\n"
    "the code runs past it, smiling\n"
    "wrong branch all along"
)

# Syllable counts for every word in the poem, so the program can check
# its own form against the gate before writing: three lines, 5-7-5,
# at most 200 characters. A haiku that fails its own check is a bug,
# and this program's whole subject is hunting those.
SYLLABLES = {
    "i": 1, "set": 1, "a": 1, "breakpoint": 2,
    "the": 1, "code": 1, "runs": 1, "past": 1, "it": 1, "smiling": 2,
    "wrong": 1, "branch": 1, "all": 1, "along": 2,
}
EXPECTED_SHAPE = [5, 7, 5]
MAX_CHARS = 200


def line_syllables(line):
    total = 0
    for token in line.replace(",", " ").split():
        word = token.lower()
        if word not in SYLLABLES:
            raise ValueError(f"no syllable count for {word!r}")
        total += SYLLABLES[word]
    return total


def check_form(text):
    lines = text.split("\n")
    if len(lines) != len(EXPECTED_SHAPE):
        raise ValueError(f"expected 3 lines, got {len(lines)}")
    shape = [line_syllables(line) for line in lines]
    if shape != EXPECTED_SHAPE:
        raise ValueError(f"syllable shape {shape}, expected {EXPECTED_SHAPE}")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"{len(text)} chars, gate allows 1..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("text is only whitespace")
    return shape


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(out_dir, "entry.txt")


def main():
    shape = check_form(HAIKU)
    path = output_path()
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(HAIKU)
    print(f"wrote {path} ({len(HAIKU)} chars, syllables {shape})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
