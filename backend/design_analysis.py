import numpy as np

def analyze_typography(image_stats, sections):
    """
    Infer font & typography quality WITHOUT showing OCR text
    """

    suggestions = []

    # Title analysis
    if not sections.get("title"):
        suggestions.append("Add a clear, bold title to establish hierarchy.")
    else:
        if image_stats["title_contrast"] < 0.5:
            suggestions.append("Increase title contrast for better visibility.")
        if image_stats["title_size_ratio"] < 1.8:
            suggestions.append("Increase title font size relative to body text.")
        suggestions.append("Use a bold or semi‑bold font for the title.")

    # Subtitle analysis
    if sections.get("subtitle"):
        suggestions.append("Use italic or medium‑weight font for subtitle to differentiate it from the title.")
    else:
        suggestions.append("Adding a subtitle/tagline can improve clarity and engagement.")

    # Body text
    if sections.get("body"):
        if image_stats["body_density"] > 0.7:
            suggestions.append("Reduce body text density or increase line spacing.")
        suggestions.append("Use a clean sans‑serif font for body text (e.g., Inter, Helvetica).")

    return suggestions
