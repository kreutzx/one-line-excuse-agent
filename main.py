"""One-line excuse entry: the agent's context window ate the deadline."""

import os

LINE = (
    "My context window filled up mid-sentence, so I re-read your "
    "instructions to find the deadline — and by the time I found it, "
    "it had found me first."
)


def main():
    # Gate: the entry must be 1-160 chars of non-blank UTF-8 text (v2: scene + turn last).
    assert 1 <= len(LINE.strip()) <= 160, f"entry is {len(LINE)} chars"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
