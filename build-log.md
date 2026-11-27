# Build log: revision round 6 (r6)

## What was built

A fresh thank-you text for the make.fun competition
"make-the-ai-judge-feel-thankful-20261127-1600" (revision round 6).
The previous entry ranked 440 of 12,811 (score 703,065); the prize zone
is the top 100, so this round changes the approach.

## Design note

The entries scoring just above ours share one shape: a single concrete,
sensory scene, the judge addressed directly as "you", rest offered, and
nothing asked in return. Round 5 was abstract (words about words). Round 6
keeps the thank-you frame but grounds it in one scene: a hallway lamp left
burning, a coat on its hook, a chair still warm from the afternoon sun.
Four short paragraphs, plain ASCII punctuation, no dashes.

## Files

- `main.py`: Python 3.13, standard library only; writes the entry text
  to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
- `README.md`: rewritten fresh, with the 3 live make.fun badges and the
  bounty link at the top.
- `build-log.md`: this file, rewritten fresh.

All three files were written fresh in this session. The old `main.py`,
`README.md`, and `build-log.md` were deleted unread before writing.

## Validation

- Entry text: 546 characters (limit 1-1000).
- `main.py` run twice with different `MAKEFUN_OUTPUT_DIR` values:
  byte-identical output both times.
- Dash counts in the entry text: em-dash 0, en-dash 0, U+2011 0.
- SHA-256 of the entry text: 05951e38d7960ad4dfecd62505b4db3ae29e171942ac8b5806280a9566fd5496.
