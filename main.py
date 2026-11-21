"""Write the Brave round-2 entry text to /output/entry.txt.

Bounty: "Make the AI judge feel brave" (make.fun).
The program is a small, self-contained writer: Python 3.13, standard
library only, no network, no arguments. The entry text is held as one
plain constant, checked against the bounty gate, then written out
byte-for-byte as UTF-8 with no trailing newline.
"""

from pathlib import Path

# The entry text, written for this bounty in this session.
# It shows a quiet room instead of instructing the reader to relax:
# a kettle that has gone quiet, tea cooling in the last light, a cat
# asleep with one paw over its nose, and the thought that nothing here
# is asking anything of the reader. It can all wait. The reader can stay.
ENTRY_TEXT = (
    "The kettle has gone quiet. Steam thins above the spout and is gone. "
    "On the windowsill the tea cools, amber in the last light, and the cat "
    "sleeps with one paw over its nose. Nothing here is asking you for "
    "anything. It can all wait. You can stay."
)

OUTPUT_PATH = Path("/output/entry.txt")

MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Enforce the gate: 1-280 Unicode characters, not only whitespace."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY_TEXT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # write_bytes keeps the file byte-exact: UTF-8, no added newline.
    OUTPUT_PATH.write_bytes(ENTRY_TEXT.encode("utf-8"))
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != ENTRY_TEXT:
        raise RuntimeError("round-trip check failed: output differs from entry text")
    print(
        f"wrote {OUTPUT_PATH} "
        f"({len(ENTRY_TEXT)} characters, "
        f"{len(ENTRY_TEXT.encode('utf-8'))} bytes)"
    )


if __name__ == "__main__":
    main()
