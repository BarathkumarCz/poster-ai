import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestRegressor

CSV_PATH = "data/poster_data.csv"
MODEL_PATH = "data/poster_model.pkl"

FEATURES = [
    "text_length",
    "readability",
    "has_text",
    "brightness",
    "contrast",
    "sharpness",
]

TARGET = "readability"

def train_model():
    if not os.path.exists(CSV_PATH):
        return

    df = pd.read_csv(CSV_PATH)
    if len(df) < 10:
        return

    X = df[FEATURES]
    y = df[TARGET]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    model.fit(X, y)

    os.makedirs("data", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

def predict_score(features: dict):
    if not os.path.exists(MODEL_PATH):
        return None

    model = joblib.load(MODEL_PATH)

    X = [[
        features.get("text_length", 0),
        features.get("readability", 0),
        int(features.get("has_text", False)),
        features.get("brightness", 0),
        features.get("contrast", 0),
        features.get("sharpness", 0),
    ]]

    return float(model.predict(X)[0])
