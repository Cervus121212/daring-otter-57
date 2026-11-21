#!/usr/bin/env python3
"""Write a one-line joke about working beside an AI coding agent.

Deterministic: the same joke is written on every run, byte for byte.
The joke is written to MAKEFUN_OUTPUT_DIR when set (the grader sets it),
else to /output, else beside this file (local development only). The
grader sandbox mounts the program directory read-only, so the program
never assumes it can write next to itself.
"""

import os

JOKE = (
    "My AI coding agent demoed itself live: it shipped the feature, "
    "deleted the tests, and thanked me for the opportunity in the "
    "commit message."
)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        here,
    ]
    last_error = None
    for out_dir in candidates:
        if not out_dir:
            continue
        try:
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
                f.write(JOKE)
            return
        except OSError as exc:  # read-only dir or missing permission: try next
            last_error = exc
            continue
    raise last_error


if __name__ == "__main__":
    main()
