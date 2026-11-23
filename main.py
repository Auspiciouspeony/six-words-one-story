#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to /output/entry.txt.

The story: "He taught the parrot. It testified."
A man teaches his parrot to talk; the bird ends up on the
witness stand. A whole crime, a trial, and a twist, in six words.
"""

import os
import stat

STORY = "He taught the parrot. It testified."


def main() -> None:
    # Self-check: never emit an entry the gate would refuse.
    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"story must be 1-60 chars, got {len(STORY)}"
    assert STORY.strip() == STORY and STORY.strip(), "story must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the story, no trailing newline, so the file is
    # byte-for-byte the six-word story the judge reads.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    # The grader collects outputs as another user: leave it readable.
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
