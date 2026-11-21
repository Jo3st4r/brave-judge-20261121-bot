"""Write the text to /output/entry.txt.

Reads MAKEFUN_OUTPUT_DIR (set by the harness); falls back to ./output.
Stdlib only, no network, deterministic: the same bytes every run.
"""

import os

TEXT = """The kettle clicks off. Steam rises, thins, is gone. Outside, rain finds the roof one drop at a time, unhurried, as if it has all evening. Nothing here needs you yet. The chair holds your weight without asking. The world will still be there when you stand."""

# The gate counts Unicode code points: 1..280, not only whitespace.
assert 1 <= len(TEXT) <= 280, len(TEXT)
assert TEXT.strip()


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
