import cv2
import numpy as np
import pytesseract
from PIL import Image
import platform
import os


# ---------------------------
# Auto‑detect Tesseract path
# ---------------------------
if platform.system() == "Windows":
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    ]
    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            break


# ---------------------------
# Image preprocessing
# ---------------------------
def preprocess_image(img: np.ndarray) -> list:
    """
    Generate multiple preprocessed versions of the image
    to improve OCR accuracy on different fonts.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    processed_images = []

    # 1. Original grayscale
    processed_images.append(gray)

    # 2. Adaptive threshold (great for posters)
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        15,
    )
    processed_images.append(thresh)

    # 3. Inverted threshold (for light text on dark bg)
    inv_thresh = cv2.bitwise_not(thresh)
    processed_images.append(inv_thresh)

    # 4. Sharpened image
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(gray, -1, kernel)
    processed_images.append(sharpened)

    return processed_images


# ---------------------------
# OCR extraction
# ---------------------------
def extract_text(image: np.ndarray) -> str:
    """
    Extract text using multiple OCR strategies
    and combine the best results.
    """
    processed_images = preprocess_image(image)

    custom_config = r"--oem 3 --psm 6"

    texts = []

    for img in processed_images:
        try:
            text = pytesseract.image_to_string(
                Image.fromarray(img),
                lang="eng",
                config=custom_config,
            )
            if text.strip():
                texts.append(text.strip())
        except Exception:
            continue

    if not texts:
        return ""

    # Remove duplicates & merge
    unique_lines = set()
    for t in texts:
        for line in t.splitlines():
            line = line.strip()
            if len(line) > 2:
                unique_lines.add(line)

    final_text = "\n".join(sorted(unique_lines))
    return final_text
