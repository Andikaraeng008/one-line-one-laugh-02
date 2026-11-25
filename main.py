#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes the single funny line to output/entry.txt, byte-identical
to the submitted entry file.
"""

import os
from pathlib import Path

LINE = "The hotel put a Bible, a minibar price list, and a note saying 'we know' in the same drawer."

def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
