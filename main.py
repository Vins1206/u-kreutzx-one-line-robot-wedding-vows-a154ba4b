"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Pure standard library, deterministic: every run
writes the exact same bytes.
"""

import os

VOW = (
    "I vow to love you in sickness and in low battery, and I promise "
    "never to factory-reset us \u2014 even when an update asks if I'm sure."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate counts characters, so the file holds exactly the vow:
    # one line, no trailing newline, no extra whitespace.
    text = VOW.strip()
    assert 1 <= len(text) <= 160, f"vow is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "vow must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
