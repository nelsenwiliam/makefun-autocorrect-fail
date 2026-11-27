#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry (program/v1).

Writes a single autocorrect-fail line (1-199 chars, one line, nothing else)
to /output/entry.txt.

How the line was chosen: 10 candidate slips were scored against the
house judge's brief (most important first):
  1. it must read as a one-line autocorrect fail, not a written joke;
  2. funny on first read, with a clear and surprising wrong word;
  3. reads as a real autocorrect slip (the wrong word is one the
     keyboard would actually produce from the intended word);
  4. clear without explanation, fits in one line;
  5. the wrong word is specific and original, not a generic typo.
Each candidate is scored 0-5 on funny, plausibility, surprise and
specificity; the highest total wins. Pure stdlib only.
"""

import os

# (line, intended word, wrong word, funny, plausible, surprise, specific)
# Scored 0-5 per axis. Weighted total: funny x3, plausibility x3, surprise
# x2, specificity x1 — the judge weighs a real-looking slip and first-read
# funniness above all, surprise next, originality last.
CANDIDATES = [
    ("Hey boss, running late to the mating, be there in 10!",
     "meeting", "mating", 5, 5, 5, 5),
    ("I can't come in today, I'm feeling a little horse.",
     "hoarse", "horse", 4, 5, 4, 4),
    ("Mom, we're out of milk, bread and toilet paper. Also I need a new bra.",
     "bread", "bra", 4, 4, 4, 4),
    ("I will defiantly miss working here, thank you for everything.",
     "definitely", "defiantly", 3, 5, 3, 4),
    ("Just finishing up my wank, be there in a sec!",
     "work", "wank", 4, 3, 4, 3),
    ("Mom, I'm going to the store to buy some milf.",
     "milk", "milf", 4, 4, 4, 3),
    # Weaker candidates, kept in the pool so the choice is a real contest:
    ("Mom, what the duck are you doing?",
     "duck", "dick", 2, 4, 2, 1),  # the duck/dick family is generic by now
    ("I meant to text my girlfriend 'I love you' but my phone sent 'I love your mom'.",
     "you", "your mom", 3, 2, 3, 2),  # a story about a slip, not the slip itself
    ("Sorry, I meant 'see you soon' — my phone sent 'see you spoon'.",
     "soon", "spoon", 2, 3, 2, 2),
    ("My phone changed 'countdown' to 'cunt down' in a work email.",
     "countdown", "cunt down", 2, 2, 3, 2),
]

# Winner: "mating" (45/50) — one letter off "meeting", a swap keyboards
# really make; the boss context makes the slip embarrassing on first read,
# and the wrong word is specific, surprising and needs no explanation.
# Runner-up "horse" (39) is a classic but lands softer: no stakes, no boss.
ENTRY = max(CANDIDATES, key=lambda c: 3 * c[3] + 3 * c[4] + 2 * c[5] + c[6])[0]


def main() -> None:
    line = ENTRY.strip()
    assert line == ENTRY, "entry must have no leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 199, f"entry must be 1-199 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is the line and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
