#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - make.fun entry.

Writes a single one-line warning label for a time machine to
/output/entry.txt. The gate requires UTF-8 text of 1 to 120
characters, not only whitespace. Deterministic, no network.
"""

import os
import sys

# The joke, by the judge's own brief: a real hazard of time travel
# (warning your past self creates a loop) turned into the punchline,
# phrased deadpan like a genuine safety notice, with the surprise
# saved for the last few words - the label you are reading IS the
# warning your past self ignored.
ENTRY_TEXT = (
    "WARNING: Do not attempt to warn yourself. "
    "The warning you are reading is the one you ignored."
)


def main() -> int:
    text = ENTRY_TEXT.strip()
    if not text:
        print("entry text is empty", file=sys.stderr)
        return 1
    if len(text) > 120:
        print(f"entry text is {len(text)} chars, over the 120 limit",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
