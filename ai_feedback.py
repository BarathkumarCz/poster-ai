def generate_ai_feedback(scores):
    """
    Generates structured AI-based design feedback from poster scores
    """

    contrast = scores.get("contrast", 0)
    readability = scores.get("readability", 0)

    feedback = {
        "contrast_feedback": "",
        "readability_feedback": "",
        "overall_comment": "",
        "rating": ""
    }

    # -------- Contrast --------
    if contrast >= 7:
        feedback["contrast_feedback"] = "Good color contrast. Text is clearly visible."
    elif contrast >= 4.5:
        feedback["contrast_feedback"] = "Moderate contrast. Increasing contrast will improve clarity."
    else:
        feedback["contrast_feedback"] = "Low contrast detected. Use darker text or lighter backgrounds."

    # -------- Readability --------
    if readability >= 8:
        feedback["readability_feedback"] = "Excellent readability and spacing."
    elif readability >= 6:
        feedback["readability_feedback"] = "Readable, but font size or spacing can be improved."
    else:
        feedback["readability_feedback"] = "Poor readability. Increase font size and line spacing."

    # -------- Overall Rating --------
    avg_score = (contrast + readability) / 2

    if avg_score >= 8:
        feedback["rating"] = "Excellent"
        feedback["overall_comment"] = "The poster is well‑designed and visually effective."
    elif avg_score >= 6:
        feedback["rating"] = "Good"
        feedback["overall_comment"] = "The poster is decent but has scope for improvement."
    else:
        feedback["rating"] = "Needs Improvement"
        feedback["overall_comment"] = "The poster requires significant design improvements."

    return feedback
