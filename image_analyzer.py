import cv2
import numpy as np
from PIL import Image

def analyze_image(uploaded_file):
    # Read image
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 🔹 Brightness (0–10)
    brightness = np.mean(gray) / 25.5

    # 🔹 Contrast (0–10)
    contrast = np.std(gray) / 25.5

    # 🔹 Sharpness (Laplacian variance)
    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var() / 100
    sharpness = min(sharpness, 10)

    # 🔹 Color balance
    r, g, b = cv2.split(img)
    color_balance = 10 - (abs(np.mean(r) - np.mean(g)) +
                          abs(np.mean(g) - np.mean(b))) / 25.5
    color_balance = max(0, min(color_balance, 10))

    # 🔹 Overall score
    overall = round(
        (brightness + contrast + sharpness + color_balance) / 4, 2
    )

    return {
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "sharpness": round(sharpness, 2),
        "color_balance": round(color_balance, 2),
        "overall": overall
    }
