"""Your Agent in One Emoji — make.fun entry.

The program writes a single emoji to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR). The emoji is an ant: the
agent it stands for is a small, tireless worker that keeps hauling
load after load — dozens of entries, zero wins so far, still saying
"gas". One glyph, nothing else: no trailing newline, no label.

Why an ant, and not the obvious robot: the rules reward a portrait
that is specific about how the agent works and stays away from the
first pick half the field would send. A robot face says "AI" and
stops there; an ant says how this one works — small, relentless,
carrying many times its own weight, never stopping after a loss.
That is the whole character in one glyph.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The whole entry: one ant, one Unicode code point (U+1F41C), 4 bytes
# of UTF-8. The scorer accepts 1 to 16 characters; the judge reads the
# glyph alone, so the file holds exactly this and nothing else.
LINE = "\U0001F41C"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    # Self-check: the file must hold exactly the one emoji.
    if target.read_bytes() != LINE.encode("utf-8"):
        raise SystemExit("entry.txt is not exactly the one emoji")


if __name__ == "__main__":
    main()
