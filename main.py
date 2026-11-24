#!/usr/bin/env python3
"""make.fun entry: The Most Honest Outage Line.

Writes one status page line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only; no third-party imports.
"""

import os

ENTRY = (
    "I can't reach any of our servers, everything is down. "
    "I don't know why yet, and I can't check anything until one responds. "
    "I'll update when I can verify more."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
