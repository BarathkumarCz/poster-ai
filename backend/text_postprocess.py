import re
import string

COMMON_JUNK = [
    "©", "|", "™", "�"
]

def clean_ocr_text(text: str) -> str:
    if not text:
        return ""

    lines = text.splitlines()
    cleaned = []

    for line in lines:
        line = line.strip()

        # remove very short garbage lines
        if len(line) < 3:
            continue

        # remove lines with too many symbols
        symbol_ratio = sum(
            1 for c in line if c in string.punctuation
        ) / max(len(line), 1)

        if symbol_ratio > 0.4:
            continue

        # remove junk characters
        for j in COMMON_JUNK:
            line = line.replace(j, "")

        # normalize spaces
        line = re.sub(r"\s+", " ", line)

        cleaned.append(line)

    return "\n".join(cleaned)
