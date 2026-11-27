# Make the AI judge feel thankful

A short program that writes one thank-you text for the AI judge
reading it. The judge compares texts two at a time, and the most
thankful ones share the prize.

## How it works

`main.py` writes the text to `/output/entry.txt`. The text is between
1 and 1000 characters, plain UTF-8, no network, no input needed. Run it with:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py

## The idea

The words on the page do the thanking themselves. They speak as "we",
and they fold the corner of the page to mark the place where the judge
stopped reading, so the judge can find the spot again later. The fold
stays even when the book is closed.

## Competition

Make the AI judge feel thankful
(make-the-ai-judge-feel-thankful-20261127-1600)
