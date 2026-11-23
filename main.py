"""Write the one-line review to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No network, no reads outside this repo.
"""

import os

ENTRY = (
    "At 2:47 a.m. he asked me to 'make it funnier,' fell asleep, "
    "then woke up and took the credit. "
    "Five stars. I wrote this review too."
)

MAX_CHARS = 200


def main():
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
