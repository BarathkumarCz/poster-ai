import cv2
import numpy as np

def analyze_image(image_array):
    # Convert RGB → Grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    # Brightness (mean pixel value)
    brightness = float(np.mean(gray)) / 25.5   # scale to ~0–10

    # Contrast
    contrast = float(np.std(gray))

    # Readability (sharpness)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    readability = min(10, laplacian_var / 100)

    return {
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "readability": round(readability, 2)
    }

