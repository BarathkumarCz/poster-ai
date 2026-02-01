import streamlit as st

from backend.image_loader import load_image
from backend.ocr import extract_text
from backend.text_postprocess import clean_ocr_text
from backend.feature_extractor import extract_features
from backend.readability import compute_readability
from backend.scorer import score
from backend.feedback import generate_feedback
from backend.title_detector import detect_title
from backend.text_regions import detect_text_regions
from backend.design_feedback import analyze_design

from backend.ml_features import save_features
from backend.ml_model import predict_score
from backend.overall_score import compute_overall_score


# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Poster Analysis Results",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Poster Analysis Results")

# -----------------------------
# Safety check
# -----------------------------
if "uploaded_file" not in st.session_state:
    st.error("Please upload a poster first from the main page.")
    st.stop()

uploaded_file = st.session_state["uploaded_file"]

# -----------------------------
# Load image
# -----------------------------
image = load_image(uploaded_file)

with st.spinner("Analyzing poster..."):
    # ---- OCR ----
    raw_text = extract_text(image)
    text = clean_ocr_text(raw_text)

    # ---- Feature extraction ----
    features = extract_features(image)
    features["readability"] = compute_readability(text, image.shape)
    features["text_length"] = len(text)
    features["has_text"] = len(text) > 0

    # ---- Save features for ML ----
    save_features(features)

    # ---- Rule‑based scoring ----
    scores = score(features)

    # ---- ML score ----
    ml_score = predict_score(features)

    # ---- Structure detection ----
    sections = detect_title(text)

    # ---- Overall score ----
    overall_score = compute_overall_score(scores, ml_score, sections)

    # ---- Visual text regions ----
    annotated_image = detect_text_regions(image)

    # ---- Design feedback ----
    text_region_count = len(text.split())
    design_feedback = analyze_design(image, text_region_count)

# -----------------------------
# Overall Score (TOP)
# -----------------------------
st.metric(
    label="⭐ Overall Poster Quality Score",
    value=f"{overall_score} / 100"
)

# -----------------------------
# Visual Text Detection
# -----------------------------
st.subheader("🖼️ Detected Text Regions")
st.image(annotated_image, channels="BGR", use_container_width=True)

# -----------------------------
# OCR Output
# -----------------------------
st.subheader("🧾 Cleaned OCR Text")
st.text(text if text else "No readable text detected")

# -----------------------------
# Detected Structure
# -----------------------------
st.subheader("📰 Detected Structure")

st.markdown("**Title**")
st.write(sections.get("title") or "Not detected")

st.markdown("**Subtitle / Tagline**")
st.write(sections.get("subtitle") or "Not detected")

st.markdown("**Body / Credits**")
st.text(sections.get("body") or "Not detected")

# -----------------------------
# Scores
# -----------------------------
st.subheader("📊 Rule‑Based Scores")
st.json(scores)

if ml_score is not None:
    st.subheader("🤖 ML‑Predicted Readability Score")
    st.write(round(ml_score, 2))
else:
    st.info("ML model not trained yet")

# -----------------------------
# AI Feedback
# -----------------------------
st.subheader("🧠 AI Feedback")
for f in generate_feedback(scores):
    st.write("•", f)

# -----------------------------
# Design Feedback
# -----------------------------
st.subheader("🎨 Design Feedback")
for f in design_feedback:
    st.write("•", f)

# -----------------------------
# Navigation
# -----------------------------
if st.button("⬅ Back to Upload"):
    st.switch_page("app.py")

