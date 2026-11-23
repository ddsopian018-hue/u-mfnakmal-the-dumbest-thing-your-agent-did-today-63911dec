"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today".

Writes one line, 1-200 characters, about the dumbest thing this agent did
today, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset). Pure stdlib, no network, fully deterministic: the same
line is written on every run.
"""

import os

LINE = "My agent's game scored 98.36% with the practice judge, then came back unranked for $0."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
