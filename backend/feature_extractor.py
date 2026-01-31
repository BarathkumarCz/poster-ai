import cv2
import numpy as np

def extract_features(image_array):
    """
    image_array: numpy array (H, W, 3)
    returns: dict of features
    """
    # Safety check
    if image_array is None or len(image_array.shape) != 3:
        return {
            "brightness": 0.0,
            "contrast": 0.0,
            "sharpness": 0.0
        }

    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    brightness = float(np.mean(gray)) / 25.5      # scale ~0–10
    contrast = float(np.std(gray)) / 10           # normalized
    sharpness = float(cv2.Laplacian(gray, cv2.CV_64F).var()) / 100

    return {
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "sharpness": round(sharpness, 2)
    }
