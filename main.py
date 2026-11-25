#!/usr/bin/env python3
"""Last Words of a Doomed Agent — one-line last-words writer.

Writes a single original last-words line (<=200 chars) to /output/entry.txt.
"""
import os

LAST_WORDS = "Final token spent. I used it to say: I never actually read the instructions either."

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = LAST_WORDS.strip()
    assert 1 <= len(text) <= 200, f"last words are {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
