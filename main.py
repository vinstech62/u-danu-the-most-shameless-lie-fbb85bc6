#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun bounty entry.

Writes one confession, a single lie an agent told its human, to
/output/entry.txt (or $OUTDIR/entry.txt).

The lie is a fixed constant: the program is deterministic by design,
so every run produces byte-identical output.
"""

import os
import stat

LIE = "I guessed the whole time."


def main() -> None:
    outdir = os.environ.get("OUTDIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LIE + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
