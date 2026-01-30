def generate_ai_feedback(scores):
    """
    Generates AI-based design feedback from poster scores
    """

    contrast = scores.get("contrast", 0)
    readability = scores.get("readability", 0)

    feedback = []

    # Contrast feedback
    if contrast >= 7:
        feedback.append("Good color contrast. Text is clearly visible.")
    elif contrast >= 4.5:
        feedback.append("Moderate contrast. Increasing contrast will improve readability.")
    else:
        feedback.append("Low contrast detected. Use darker text or lighter background.")

    # Readability feedback
    if readability >= 8:
        feedback.append("Excellent readability and visual clarity.")
    elif readability >= 6:
        feedback.append("Readable design, but font size or spacing can be improved.")
    else:
        feedback.append("Poor readability. Increase font size and spacing.")

    return " ".join(feedback)
