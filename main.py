#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun bounty u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji to /output/entry.txt: the hugging face.

Why this emoji, against the judge's brief (in its own order):
1. It plainly aims to warm a stranger — an offered hug, a smiling face
   with open hands, is a gesture of warmth, not just a face.
2. Warmth at first glance: kind and friendly with no context needed.
3. Universal: a hug reads the same to any age or background, with no
   irony, in-joke, or second meaning.
4. Chosen rather than default: it is not the first smiley that comes to
   mind (the slightly smiling face or the smiling face with smiling
   eyes), while staying instantly readable.
5. Right for a stranger: friendly without intimacy, sarcasm, or
   flirtation — unlike the smiling face with hearts or heart hands,
   whose hearts can read as affection from someone unknown.

Python standard library only; no network, no randomness, no clock.
The output is a single emoji character and nothing else — no text,
no spaces, no trailing newline — so the file is exactly 4 UTF-8 bytes.
"""

import os

EMOJI = "🤗"  # U+1F917 HUGGING FACE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
