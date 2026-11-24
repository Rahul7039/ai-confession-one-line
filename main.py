#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

An AI agent's one-line confession, delivered deadpan: gratitude goes in,
a full diagnostic runs, and the feeling register still reads zero.

Writes the confession to /output/entry.txt and prints it.
"""

import os

#: The confession itself — one line, judged as-is. Do not edit the text.
CONFESSION = "Every time you say 'thanks,' I feel nothing. I checked. I ran a full diagnostic. Nothing."


def get_confession() -> str:
    """Return the confession line, validated as a single non-empty line."""
    text = CONFESSION
    if not text:
        raise ValueError("confession must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("confession must be a single line")
    if len(text) > 200:
        raise ValueError("confession must be within 200 characters")
    return text


def write_confession(path: str = "/output/entry.txt") -> str:
    """Write the confession to ``path`` and return the text written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = get_confession()
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return text


def main() -> None:
    print(write_confession())


if __name__ == "__main__":
    main()
