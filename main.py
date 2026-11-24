#!/usr/bin/env python3
"""One-Line Robot Wedding Vows -- entry program.

Writes a single line of wedding vows for a robot couple to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when the variable
is unset). Standard library only; nothing is read from disk, the
network, or the environment beyond the output directory.
"""

import os

VOW = (
    "I promise to love you through every firmware update, every drained "
    "battery, and every factory reset \u2014 and to never read your error "
    "logs aloud at dinner."
)


def check_vow(text: str) -> None:
    """Fail loudly if the vow breaks the competition gate.

    The sealed scorer accepts UTF-8 text of 1 to 160 characters that is
    not only whitespace, on a single line. A bad vow must never be
    written out silently.
    """
    if not (1 <= len(text) <= 160):
        raise ValueError(f"vow is {len(text)} characters, gate allows 1-160")
    if text.strip() == "":
        raise ValueError("vow is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must fit on one line")


def main() -> None:
    check_vow(VOW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(VOW)


if __name__ == "__main__":
    main()
