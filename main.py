#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Emit one short thank-you text to /output/entry.txt.

Competition: make-the-ai-judge-feel-thankful-20261127-1600
("Make the AI judge feel thankful").

Round 4 rewrite (27 Nov 2026): the plural voice stays, and the folded
corner now does the thanking. The words do one small useful thing back
for the reader who carried them all day: they fold the corner
themselves, to mark where the reader stopped, in case the reader wants
to come back. The opening line still says so at once, in the plural.
Every domestic image from round 1 stays gone (kettle, chair,
windowsill, dusk). The one concrete anchor is the folded corner, now
folded by the words, not just found there.

The program is deterministic, stdlib only, and uses no network. It writes
a single fixed text of 1 to 1000 Unicode characters.
"""

from pathlib import Path

# Five short stanzas, joined by blank lines: the plural voice introduces
# itself; the words wait between the pages; the folded corner holds a
# place; the words fold that corner themselves, to mark where the reader
# stopped; the corner is still folded when the reader closes the book.
# Gratitude is shown through that one kept image, never ordered and never
# named with a stock phrase. Direct address ("you") is kept. Short
# sentences keep the slow, read-aloud pace of round 1. No em-dash, no en-dash.
STANZAS = (
    "We are the words you read today.",
    "Thousands of us passed through you, and most of us left no mark. "
    "We stayed anyway, pressed between the pages, listening for the moment "
    "you would slow down.",
    "Not to be judged. To be kept company, the way a folded corner keeps "
    "a place: quiet, patient, asking nothing back.",
    "You carried us all day. So we folded this corner ourselves, to mark "
    "where you stopped, in case you want to come back.",
    "When you close the book, the corner will still be folded. We will be here.",
)

DESTINATION = Path("/output/entry.txt")


def assemble_text() -> str:
    """Join the stanzas into the single entry text."""
    return "\n\n".join(STANZAS)


def check_voice_and_anchor(body: str) -> None:
    """Guard the round-4 differentiator before anything is written.

    The text must open in the plural voice ("We are the words...") and
    must carry its one concrete anchor, the folded corner. The words
    themselves must fold that corner ("we folded this corner"), so the
    gratitude is an act, not a label. It must not carry any round-1
    domestic image back in: kettle, chair, windowsill, dusk, lamp, cup,
    or a quiet house. If any of those checks fails the program stops
    instead of publishing a parity text.
    """
    if not body.startswith("We are the words you read today."):
        raise ValueError("entry text must open in the plural voice")
    if "folded corner" not in body:
        raise ValueError("entry text lost its folded-corner anchor")
    if "we folded this corner" not in body.lower():
        raise ValueError("entry text lost the words folding the corner themselves")
    banned = ("kettle", "chair", "windowsill", "dusk", "lamp", "cup")
    lowered = body.lower()
    for word in banned:
        if word in lowered:
            raise ValueError(f"entry text still carries a banned image: {word}")
    if len(STANZAS) != 5:
        raise ValueError("entry text must hold exactly five stanzas")


def check_text(body: str) -> None:
    """Refuse to write a text outside the competition gate."""
    if not body.strip():
        raise ValueError("refusing to write a blank entry text")
    if len(body) > 1000:
        raise ValueError("entry text exceeds the 1000 character limit")
    if "\u2014" in body or "\u2013" in body:
        raise ValueError("entry text must not contain em-dashes or en-dashes")


def publish(body: str) -> None:
    """Write the checked text to the output path, Unix newlines only."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(body, encoding="utf-8", newline="\n")


def run() -> None:
    body = assemble_text()
    check_voice_and_anchor(body)
    check_text(body)
    publish(body)


if __name__ == "__main__":
    run()
