#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short, quiet text to /output/entry.txt: a still evening scene
the reader can rest in. No network, no randomness, no external files.
"""

import os

TEXT = (
    "The kettle has gone quiet. The cup in your hands is still warm, "
    "and outside the window the light is leaving the rooftops one by one. "
    "Nothing here is asking anything of you. "
    "The evening settles into the room and stays, "
    "the way the warmth stays in the cup."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
