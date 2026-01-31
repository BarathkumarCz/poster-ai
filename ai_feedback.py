def generate_ai_feedback(scores):
    feedback = []

    if scores["brightness"] < 5:
        feedback.append("Increase brightness to improve visibility.")
    else:
        feedback.append("Brightness level is good.")

    if scores["contrast"] < 5:
        feedback.append("Improve contrast so text stands out.")
    else:
        feedback.append("Contrast is well balanced.")

    if scores["sharpness"] < 5:
        feedback.append("Poster looks blurry. Use higher resolution images.")
    else:
        feedback.append("Sharpness is good.")

    if scores["color_balance"] < 5:
        feedback.append("Colors are unbalanced. Try a consistent color palette.")
    else:
        feedback.append("Color balance looks appealing.")

    feedback.append(f"Overall poster score: {scores['overall']}/10")

    return " ".join(feedback)
