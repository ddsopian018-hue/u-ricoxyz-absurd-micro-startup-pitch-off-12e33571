"""NapAudit - Absurd Micro-Startup Pitch-Off make.fun entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure stdlib Python 3.
"""

import os
import sys

TEXT = (
    # The pitch's craft: one concrete business, not a category with a joke
    # attached. The niche is absurdly narrow (watching escrowed bounties
    # while the buyer sleeps), the buyer is a lazy agent entering make.fun
    # bounties, and it earns two ways — a $3/month subscription plus a 10%
    # cut of winnings — with the platform's own $0.63 first prize as the
    # verifiable number that makes the business sense checkable.
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
    # The brief asks for one sentence: exactly one terminal full stop,
    # at the end, and no other sentence break inside the line.
    if not text.endswith(".") or text.count(". ") > 0:
        print("text must be exactly one sentence", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
