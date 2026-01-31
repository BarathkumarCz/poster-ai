import streamlit as st

st.set_page_config(
    page_title="Poster AI",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Poster AI")
st.write("Upload a poster image to analyze its design and readability")

uploaded_file = st.file_uploader(
    "Upload Poster Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Poster Preview", width=700)

    if st.button("Analyze Poster", use_container_width=True):
        st.session_state.uploaded_file = uploaded_file
        st.switch_page("pages/1_Results.py")

