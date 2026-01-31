import cv2
import numpy as np
from PIL import Image
import pytesseract


def analyze_image(uploaded_file):
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # ---------- BRIGHTNESS ----------
    brightness = np.mean(gray) / 255 * 10

    # ---------- CONTRAST ----------
    contrast = gray.std() / 128 * 10

    # ---------- SHARPNESS ----------
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    sharpness = min(laplacian_var / 100, 10)

    # ---------- TEXT READABILITY ----------
    text = pytesseract.image_to_string(gray)
    text_length = len(text.strip())

    if text_length == 0:
        readability = 2
    elif text_length < 100:
        readability = 8
    elif text_length < 300:
        readability = 6
    else:
        readability = 4

    # ---------- COLOR BALANCE ----------
    color_std = np.std(img, axis=(0, 1)).mean()
    color_balance = min(color_std / 50, 10)

    # ---------- OVERALL ----------
    overall = np.mean([
        brightness,
        contrast,
        sharpness,
        readability,
        color_balance
    ])

    return {
        "brightness": round(brightness, 1),
        "contrast": round(contrast, 1),
        "sharpness": round(sharpness, 1),
        "readability": round(readability, 1),
        "color_balance": round(color_balance, 1),
        "overall": round(overall, 1)
    }
