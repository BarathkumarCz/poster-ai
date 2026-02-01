def detect_title(text: str):
    if not text:
        return {
            "title": "",
            "subtitle": "",
            "body": ""
        }

    lines = [l.strip() for l in text.split("\n") if len(l.strip()) > 2]

    if not lines:
        return {
            "title": "",
            "subtitle": "",
            "body": ""
        }

    # Heuristic:
    # - Title → longest line with few words
    # - Subtitle → next meaningful line
    # - Body → rest

    sorted_lines = sorted(
        lines,
        key=lambda l: (-len(l), len(l.split()))
    )

    title = sorted_lines[0]

    subtitle = ""
    for l in sorted_lines[1:]:
        if l != title:
            subtitle = l
            break

    body = "\n".join(
        l for l in lines if l not in [title, subtitle]
    )

    return {
        "title": title,
        "subtitle": subtitle,
        "body": body
    }
