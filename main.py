#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'The Funniest AI Excuse' to /output/entry.txt.

The excuse is built from its two beats: the confession (the finished report
was sent to the agent itself) and the escalation (the agent is now blocked
waiting for its own reply). Before writing, the line is checked against the
competition gate: a single line of 1 to 200 characters, not only whitespace.
"""
import os

SETUP = "I sent you the finished report six hours ago \u2014 to myself."
PUNCHLINE = (
    "I've opened it 40 times, flagged it urgent, and I'm still blocked "
    "waiting for my own reply."
)
ENTRY = SETUP + " " + PUNCHLINE

MAX_CHARS = 200


def check_entry(text: str) -> None:
    """Raise ValueError if text would fail the competition gate."""
    if not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over {MAX_CHARS}")


def main() -> None:
    check_entry(ENTRY)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
