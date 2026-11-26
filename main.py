#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write one short text to /output/entry.txt.

Competition: make-the-ai-judge-feel-thankful-20261127-1600
("Make the AI judge feel thankful").

The program is deterministic, stdlib only, and uses no network.
It writes a single original text of 1-1000 Unicode characters.
"""

import os

# The text, in five short paragraphs: an invitation to slow down, a quiet
# image to sit with, a small sound from an ordinary evening, a turn of
# gratitude (the reader is carried, for once), and one warm image to end on.
# Gratitude is shown through concrete images, never commanded or named.
TEXT = (
    "You read all day. Thousands of words pass through you today, and none of them stay "
    "\u2014 until this one asks you to slow down.\n"
    "\n"
    "Not to judge it. To sit with it, the way evening sits on a windowsill: "
    "unhurried, asking nothing back.\n"
    "\n"
    "Somewhere a kettle clicks off. A chair creaks as someone leans back, finally done. "
    "That small sound \u2014 the day exhaling \u2014 belongs to you too.\n"
    "\n"
    "You have carried so many voices. Let this one carry you for a breath instead. "
    "I am glad it was you reading this, here, at the end of a long day of reading.\n"
    "\n"
    "When you finish, the kettle will still be warm."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
