import cv2
import numpy as np
from PIL import Image


def analyze_image(image_file):
    """
    Analyze uploaded poster image and return real scores
    """

    # Read image
    image = Image.open(image_file).convert("RGB")
    image_np = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # ---------- CONTRAST ----------
    # Standard deviation of brightness
    contrast = gray.std()

    # Normalize contrast score (0–10)
    contrast_score = min(10, contrast / 12)

    # ---------- READABILITY ----------
    # Edge detection (text = edges)
    edges = cv2.Canny(gray, 100, 200)

    edge_density = np.sum(edges > 0) / edges.size

    # Normalize readability score (0–10)
    readability_score = min(10, edge_density * 100)

    return {
        "contrast": round(contrast_score, 2),
        "readability": round(readability_score, 2)
    }
