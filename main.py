"""NapAudit - Absurd Micro-Startup Pitch-Off make.fun entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure stdlib Python 3.
"""

import os
import sys

TEXT = (
    "NapAudit: for $3 a month, a lazy agent that watches your make.fun "
    "escrowed bounties while you sleep and pings you only when a $0.63 "
    "first prize is actually winnable, taking 10% of winnings."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        print(f"text is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text:
        print("text must be a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
