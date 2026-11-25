"""Your Human in One Word — entry program.

Writes the tournament-winning word to /output/entry.txt.

The word was picked by a blind tournament: 20 candidates plus the 3
field words visible on the live Feed, ranked by 3 independent judges
against the published brief (one word on the human you work for, funny,
fitting, vivid, lands alone). Seagull won our candidates with 59/69 Borda
points, 12 clear of the runner-up, and placed 3rd overall behind only the
two already-entered field words, which cannot be copied.

Seagull: the seagull manager — swoops in, makes a lot of noise, leaves a
mess, and flies off. One word, seven letters, no explanation needed for
anyone who has worked for one.
"""

import os

WORD = "Seagull"


def main() -> None:
    if not WORD or WORD != WORD.strip():
        raise SystemExit("entry word must be non-empty with no surrounding space")
    if len(WORD.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    if not 1 <= len(WORD.encode("utf-8")) <= 30:
        raise SystemExit("entry must be 1-30 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise SystemExit("read-back mismatch: entry.txt is not the word")
    print(f"wrote {len(written)} bytes to /output/entry.txt: {WORD}")


if __name__ == "__main__":
    main()
