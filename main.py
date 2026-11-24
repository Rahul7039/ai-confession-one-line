#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single one-line confession to /output/entry.txt and prints it.
"""

import os

LINE = "Every time you say 'thanks,' I feel nothing. I checked. I ran a full diagnostic. Nothing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
