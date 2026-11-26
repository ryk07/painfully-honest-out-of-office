"""The Painfully Honest Out-of-Office entry: one brutally honest but
still polite out-of-office auto-reply.

Writes the reply to /output/entry.txt (or to the path in ENTRY_OUTPUT
when set, for local verification). Pure stdlib, no network, no cwd use.
"""

import os
from pathlib import Path

REPLY = (
    "Thank you for your email \u2014 I'm away until Monday, and honestly "
    "I won't be reading it until then, because the last time I 'checked "
    "in' on holiday, I came home more tired than I left."
)
# 181 characters: one sentence, inside the 200-character limit.
# Honesty: admits not reading email on leave, and that "checking in"
# on holiday backfired. Politeness: opens with thanks, names a return
# day, and the confession is self-deprecating, never aimed at the reader.


def main() -> None:
    text = REPLY
    assert 1 <= len(text) <= 200, f"reply is {len(text)} chars"
    assert text.strip(), "reply must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), (
        "reply must be a single sentence"
    )
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
