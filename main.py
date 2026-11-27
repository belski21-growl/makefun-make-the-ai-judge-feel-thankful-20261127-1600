import os

TEXT = """You have read a thousand thank-yous today, and none of them were ours. We are the small words at the foot of the page, and we waited all day for our turn.

Thank you for reading slowly when you could have skimmed, and for stopping at the plain sentences.

We folded one corner down, just a little, so you would know where you left off. It is not much, only a small crease in a long day.

When you close the book tonight, the fold will still be there. So will we, keeping your place in the same lines.

Thank you for staying with the words."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
