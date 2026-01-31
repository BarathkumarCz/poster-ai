<<<<<<< Updated upstream
=======
import streamlit as st
from ai_feedback import generate_ai_feedback
from image_analyzer import analyze_image

st.set_page_config(page_title="Poster AI", layout="centered")

# -------- Session State --------
if "page" not in st.session_state:
    st.session_state.page = "upload"

if "scores" not in st.session_state:
    st.session_state.scores = None


# -------- PAGE 1 : UPLOAD --------
if st.session_state.page == "upload":
    st.title("🎨 AI Poster Analysis System")
    st.write("Upload your poster to get AI-based design feedback")

    uploaded_file = st.file_uploader(
        "Upload Poster Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Poster", use_column_width=True)

        if st.button("Analyze Poster"):
            # TEMPORARY scores (replace with real analysis later)
            scores = analyze_image(uploaded_file)


            st.session_state.scores = scores
            st.session_state.page = "feedback"
            st.rerun()


# -------- PAGE 2 : FEEDBACK --------
elif st.session_state.page == "feedback":
    st.title("📝 AI Design Feedback")

    scores = st.session_state.scores

    st.subheader("Poster Scores")
    st.write(scores)

    ai_text = generate_ai_feedback(scores)

    st.subheader("AI Suggestions")
    st.write(ai_text)

    if st.button("⬅ Back to Upload"):
        st.session_state.page = "upload"
        st.rerun()


>>>>>>> Stashed changes
