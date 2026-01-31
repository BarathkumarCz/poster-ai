def generate_ai_feedback(scores):
    feedback = []

    if scores["brightness"] < 4:
        feedback.append("🔆 Increase brightness to improve visibility.")
    else:
        feedback.append("✅ Brightness level is good.")

    if scores["contrast"] < 20:
        feedback.append("🎨 Increase contrast for better text separation.")
    else:
        feedback.append("✅ Contrast looks balanced.")

    if scores["sharpness"] < 4:
        feedback.append("📐 Poster looks blurry. Improve image sharpness.")
    else:
        feedback.append("✅ Image sharpness is good.")

    if scores["readability"] < 5:
        feedback.append("📝 Improve font clarity and spacing.")
    else:
        feedback.append("✅ Text readability is strong.")

    return "\n".join(feedback)
