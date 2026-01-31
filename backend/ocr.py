import cv2
import numpy as np
import pytesseract
from PIL import Image

# ✅ Explicit path for Windows (fixes TesseractNotFoundError)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_array):
    """
    image_array: NumPy array (H x W x C) from Streamlit upload
    returns: extracted text (string)
    """

    if image_array is None:
        return ""

    # Ensure uint8 format
    if image_array.dtype != np.uint8:
        image_array = image_array.astype(np.uint8)

    # Convert to grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

    # Optional preprocessing for better OCR
    gray = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    try:
        text = pytesseract.image_to_string(gray)
        return text.strip()
    except Exception as e:
        return f"OCR Error: {str(e)}"
