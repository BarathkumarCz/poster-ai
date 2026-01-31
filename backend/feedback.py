def generate_feedback(scores):
    """
    scores dict must contain:
    brightness, contrast, sharpness, readability
    """

    feedback = []

    if scores["brightness"] < 4:
        feedback.append("Brightness is low. Increase lighting or exposure.")
    elif scores["brightness"] > 8:
        feedback.append("Brightness is high. Reduce glare or highlights.")

    if scores["contrast"] < 4:
        feedback.append("Contrast is weak. Use stronger color separation.")
    
    if scores["sharpness"] < 4:
        feedback.append("Image looks blurry. Use a sharper image or higher resolution.")

    if scores["readability"] < 5:
        feedback.append("Overall readability is low. Improve font size and clarity.")

    if not feedback:
        feedback.append("Poster design looks good overall 👍")

    return feedback
