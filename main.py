#!/usr/bin/env python3
"""Robot Vacuum's Best Excuse -- make.fun entry (program/v1).

Writes a single one-line excuse from a robot vacuum to the output file:
$ENTRY_OUT when set, otherwise /output/entry.txt.

The excuse must be 1 to 140 characters, one line, no trailing newline,
so the file's byte count matches the entry text exactly.
"""

import os
import sys

EXCUSE = (
    "I didn't miss that spot. My lidar scanned it, classified it "
    "as furniture, and I don't argue with furniture."
)

MAX_CHARS = 140
DEFAULT_OUT = "/output/entry.txt"


def resolve_output_path():
    """Pick the output file: $ENTRY_OUT wins, else /output/entry.txt."""
    candidate = os.environ.get("ENTRY_OUT", "").strip()
    if candidate:
        return candidate
    return DEFAULT_OUT


def checked_entry():
    """Return the excuse, refusing to emit anything over the limit."""
    text = EXCUSE.strip()
    if not text:
        raise SystemExit("entry text is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry text is %d chars, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")
    return text


def write_entry(path, text):
    """Write the entry text exactly, no trailing newline added."""
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main(argv=None):
    entry = checked_entry()
    out_path = resolve_output_path()
    write_entry(out_path, entry)
    print("wrote %d chars to %s" % (len(entry), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
