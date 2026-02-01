import csv
import os
from datetime import datetime

DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "poster_data.csv")

HEADERS = [
    "text_length",
    "readability",
    "has_text",
    "brightness",
    "contrast",
    "sharpness",
    "timestamp",
]

def save_features(features: dict):
    os.makedirs(DATA_DIR, exist_ok=True)
    file_exists = os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "text_length": features.get("text_length", 0),
            "readability": features.get("readability", 0),
            "has_text": int(features.get("has_text", False)),
            "brightness": features.get("brightness", 0),
            "contrast": features.get("contrast", 0),
            "sharpness": features.get("sharpness", 0),
            "timestamp": datetime.now().isoformat(),
        })
