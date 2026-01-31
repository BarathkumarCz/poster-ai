import cv2
import numpy as np

def analyze_image(image_array):
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    brightness = float(np.mean(gray)) / 25.5
    contrast = float(np.std(gray))

    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    sharpness = min(10, laplacian_var / 100)

    return {
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "sharpness": round(sharpness, 2),
        "readability": round(sharpness, 2)  # safe alias
    }
