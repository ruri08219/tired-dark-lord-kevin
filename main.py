#!/usr/bin/env python3
"""Write the 100-word villain monologue to /output/entry.txt.

Stdlib only. The monologue is exactly 100 words and 559 characters,
inside the gate's 1-600 character window.
"""
import os
import sys

MAX_CHARS = 600
EXPECTED_WORDS = 100

ENTRY = (
    "Hero, sit. Not the throne, the stool. The throne squeaks, and I have "
    "endured three centuries of squeaks. You came for the Ashen Crown, the "
    "one I forged from the last eclipse, the one that drinks light from "
    "candles. Take it. It weighs eleven pounds, and my neck has filed a "
    "complaint. I meant to conquer the coast this spring. Then the ravens "
    "needed feeding, the kettle cracked, the stairs grew another flight. "
    "Conquest waits. Everything waits. The crown is yours. Carry it down "
    "the stairs for me, would you? My knees remember every step. The door "
    "is that way."
)


def main():
    words = ENTRY.split()
    if len(words) != EXPECTED_WORDS:
        raise SystemExit(
            f"entry must be {EXPECTED_WORDS} words, got {len(words)}"
        )
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            f"entry must be at most {MAX_CHARS} chars, got {len(ENTRY)}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY.split())} words, {len(ENTRY)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
