import streamlit as st

from backend.image_loader import load_image
from backend.feature_extractor import extract_features
from backend.scorer import score
from backend.feedback import generate_feedback
from backend.ocr import extract_text
from backend.readability import compute_readability

st.set_page_config(
    page_title="Results | Poster AI",
    layout="centered"
)

st.title("📊 Poster Analysis Results")

if "uploaded_file" not in st.session_state:
    st.warning("No poster found. Please upload a poster first.")
    st.stop()

uploaded_file = st.session_state.uploaded_file

st.image(uploaded_file, caption="Analyzed Poster", width=700)

with st.spinner("Analyzing poster..."):
    image_array = load_image(uploaded_file)
    text = extract_text(image_array)

    features = extract_features(image_array)
    features["readability"] = compute_readability(
        text,
        image_array.shape
    )

    scores = score(features)
    feedback = generate_feedback(scores)

tab1, tab2, tab3 = st.tabs(["Scores", "OCR Text", "AI Feedback"])

with tab1:
    st.json(scores)

with tab2:
    st.text_area(
        "Detected Text",
        text if text else "No readable text detected",
        height=300
    )

with tab3:
    if feedback:
        for f in feedback:
            st.write("•", f)
    else:
        st.write("No feedback generated")

if st.button("⬅ Upload Another Poster", use_container_width=True):
    st.switch_page("app.py")
