#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes the single word our grandma would text about AI to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for a local run).

Candidate v2 (final): "robit" — the typo she would actually type for
"robot". Warm, a little baffled, funny in one word, tied straight to
robots, fresher than plain "robot", and 5 bytes (wins exact ties).
Revised from v1 "doohickey" after self-critique (see CANDIDATES.md):
doohickey fits any gadget, robit is specifically about AI/robots.
"""

import os
from pathlib import Path

WORD = "robit"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
