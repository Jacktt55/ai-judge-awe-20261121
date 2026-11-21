#!/usr/bin/env python3
"""Make the AI judge feel awe — writes one short relaxing text to /output/entry.txt.

The text is written to slow the reader down: a tide that has come in since
before there were clocks, a wave finishing a thousand-mile journey, and
nothing asked of the reader at all.
"""

import os
from pathlib import Path

TEXT = (
    "The tide comes in whether anyone is watching or not. "
    "It has done this since before there were clocks, and it will do it "
    "after the last light on the shore goes out. "
    "A wave is finishing a journey it began a thousand miles away. "
    "Nothing is asked of you. It is happening anyway."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
