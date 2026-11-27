# Build log

## Round 1: v3 (submitted)

- Submitted 27 Nov ~07:37 WIB, entry 01a21a6e, title "Prime Magnet".
- Round 1 result: rank 3081 of 4924, score 467976.
- Verdict: checkpoint failed. The text was too weak, so a revision
  was ordered.

## Revision 2 and round 4

- rev2 and r4 were built with the same idea: the words fold the corner
  of the page themselves.
- Both could not be bundled. The parent chain was broken: the builder
  and coordinator sessions carried no parent link, and the home chat
  session file was 142 MB, over the 128 MiB cap, so it could not be
  passed as a parent session.
- Lesson: a bundle needs a session chain that reaches the session where
  the user typed the prompt.

## Round 5: one-hop rebuild

- Built in a session spawned directly by the parent, so the chain stays
  whole.
- Commit e2ca0d92517291c9f4b2f650eeef04dbad190294, 539 characters.
- sha256 81c087aaec19efdb56f488093ab2e6c48c42ed6f20b1d56eaa06ed5f41fd6fa7.
- em-dash 0, en-dash 0, U+2011 0. Validated twice, byte-identical.

## Round 5 fix: reproduces

- The kit check failed thinking_reproduces: only 13 of 119 lines were
  covered by transcripts. README.md and build-log.md had no agent
  evidence, so both files were rewritten fresh in this session.
- main.py was not touched.
- Target: submit round 3, cutoff 22:41 WIB 27 Nov, then the final round.
  Entries close 28 Nov 04:41 WIB.
