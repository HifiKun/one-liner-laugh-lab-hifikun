#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

Writes a single funny line (at most 200 characters) answering the prompt:
the excuse a robot vacuum gives after eating a sock.
"""

import os

LINE = "I didn't eat your sock — I adopted it. It lives under the couch now and pays rent in dust."

# The sealed gate only accepts 1 to 200 characters, so refuse to write
# anything outside it instead of submitting an invalid entry.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, must be 1-200"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"Wrote {len(LINE)} characters to /output/entry.txt")
