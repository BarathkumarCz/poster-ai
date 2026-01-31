import pytesseract
import cv2
import numpy as np

# For Apple Silicon Macs (already installed in step 1)
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def extract_text(image_array):
    """
    image_array: NumPy array (H x W x C)
    returns: extracted text (string)
    """

    # Convert RGB → Grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    # Improve contrast for OCR
    gray = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2
    )

    # OCR
    text = pytesseract.image_to_string(gray)

    return text.strip()
