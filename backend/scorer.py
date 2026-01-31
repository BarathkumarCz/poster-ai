def score(features):
    """
    features: dict from extract_features
    returns: scores dict with fixed keys
    """

    brightness = features.get("brightness", 0)
    contrast = features.get("contrast", 0)
    sharpness = features.get("sharpness", 0)

    # Simple rule-based scoring (0–10)
    brightness_score = min(brightness, 10)
    contrast_score = min(contrast, 10)
    sharpness_score = min(sharpness, 10)

    # Readability (derived metric)
    readability = round(
        (brightness_score + contrast_score + sharpness_score) / 3, 2
    )

    return {
        "brightness": round(brightness_score, 2),
        "contrast": round(contrast_score, 2),
        "sharpness": round(sharpness_score, 2),
        "readability": readability
    }
