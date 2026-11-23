#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes exactly one six-word story to /output/entry.txt.

The story: "He remembered everything. Except her name."
A man whose memory is perfect — except for the one name that
mattered most. A whole life, a marriage, and a mind failing,
in six words: the twist lands in the final two.
"""

import os

STORY = "He remembered everything. Except her name."


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
    # The grader collects outputs as another user: leave the file readable.
    # (Only chmod the file we created; the /output directory itself is
    # owned by the sandbox, and chmodding it fails as an unprivileged user.)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
