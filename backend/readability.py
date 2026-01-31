def compute_readability(text, image_shape):
    """
    text: OCR extracted string
    image_shape: image_array.shape -> (H, W, C)
    returns: score (0–10)
    """

    h, w, _ = image_shape
    image_area = h * w

    text_len = len(text.strip())

    if text_len == 0:
        return 0  # no readable text

    # text density heuristic
    density = text_len / image_area

    score = 10

    # too little text
    if text_len < 30:
        score -= 4

    # too much text
    if text_len > 800:
        score -= 3

    # very dense posters are hard to read
    if density > 0.002:
        score -= 3

    return max(0, min(10, score))
