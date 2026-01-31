import streamlit as st

from backend.image_loader import load_image
from backend.feature_extractor import extract_features
from backend.scorer import score
from backend.feedback import generate_feedback
from backend.ocr import extract_text
from backend.readability import compute_readability

st.set_page_config(page_title="Poster AI", layout="centered")

st.title("🎨 AI Poster Analysis System")
st.write("Upload a poster to get AI-based design + readability feedback")

uploaded_file = st.file_uploader(
    "Upload Poster Image",
    type=["png", "jpg", "jpeg"]
)

st.caption("🔍 Analysis uses full‑resolution image")

if uploaded_file is not None:
    # UI display (scaled only for screen)
    st.image(
        uploaded_file,
        caption="Uploaded Poster (display scaled, analysis uses full resolution)",
        width=800
    )

    if st.button("Analyze Poster"):
        # ---- Load high‑resolution image ----
        image_array = load_image(uploaded_file)

        # ---- OCR ----
        text = extract_text(image_array)
        st.subheader("🧾 Detected Text (OCR)")
        st.text(text if text else "No readable text detected")

        # ---- Visual features ----
        features = extract_features(image_array)

        # ---- Readability (OCR‑based) ----
        features["readability"] = compute_readability(
            text,
            image_array.shape
        )

        # ---- Optional OCR metadata ----
        features["text_length"] = len(text)
        features["has_text"] = len(text) > 0

        # ---- Scoring ----
        scores = score(features)

        st.subheader("📊 Poster Scores")
        st.json(scores)

        # ---- AI Feedback ----
        feedback = generate_feedback(scores)

        st.subheader("🧠 AI Suggestions")
        for f in feedback:
            st.write("•", f)
