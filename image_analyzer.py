import cv2
import numpy as np

def analyze_image(image_array):
    """
    image_array: NumPy array (H x W x C)
    returns: dict of scores
    """

    # Safety check
    if image_array is None:
        return {"error": "No image received"}

    # Convert RGB → Grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    # ---- Contrast score ----
    contrast = float(np.std(gray))

    # ---- Sharpness / readability ----
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    readability = min(10, laplacian_var / 100)

    return {
        "contrast": round(contrast, 2),
        "readability": round(readability, 2)
    }
