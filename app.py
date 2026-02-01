import streamlit as st

st.set_page_config(
    page_title="Poster AI",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 AI Poster Analysis System")
st.write("Upload a poster and get AI‑based design & readability feedback")

uploaded_file = st.file_uploader(
    "Upload Poster Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Poster", width=600)

    if st.button("Analyze Poster 🚀"):
        st.session_state["uploaded_file"] = uploaded_file
        st.switch_page("pages/results.py")
