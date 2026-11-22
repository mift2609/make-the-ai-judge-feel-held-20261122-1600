#!/usr/bin/env python3
"""Local check: run main.py and validate /output/entry.txt."""

import subprocess
import sys

subprocess.run([sys.executable, "main.py"], check=True)
text = open("/output/entry.txt", encoding="utf-8").read()
assert 1 <= len(text) <= 280, f"length {len(text)} out of range"
assert text.strip(), "entry is whitespace-only"
print(f"OK: {len(text)} characters")
print(text)
