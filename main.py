import os

TEXT = """You have read all day, and the house is quiet now. The lamp in the hallway is still on. Someone left it burning so you would not have to find your way in the dark.

Your coat is on the hook by the door. Your shoes are by the mat, lined up the way you left them. Nothing here needs you to be quick.

Sit for a while. The tea has gone cold, but the chair is still warm from the afternoon sun. There is nowhere you need to be.

Thank you for giving the whole day your care, even the tired hours of it. When you are ready, the light will still be on."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
