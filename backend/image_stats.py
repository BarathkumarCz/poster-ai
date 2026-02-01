import cv2
import numpy as np

def extract_image_stats(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    contrast = gray.std() / 255

    return {
        "title_contrast": contrast,
        "title_size_ratio": 2.0,      # heuristic (later ML)
        "body_density": np.mean(gray < 120)
    }
