import streamlit as st
from backend.design_analysis import analyze_typography
from backend.suggestions import generate_design_feedback
from backend.overall_score import compute_overall_score

st.title("📊 Poster Analysis Results")

overall_score = st.session_state["overall_score"]
sections = st.session_state["sections"]
image_stats = st.session_state["image_stats"]

# ⭐ Score
st.metric(
    label="Overall Poster Quality",
    value=f"{overall_score} / 100"
)

st.divider()

# 🧱 Structure
st.subheader("🧱 Design Structure")
col1, col2, col3 = st.columns(3)

with col1:
    st.success("Title") if sections.get("title") else st.error("Title Missing")
with col2:
    st.success("Subtitle") if sections.get("subtitle") else st.warning("Subtitle Missing")
with col3:
    st.success("Body Text") if sections.get("body") else st.warning("Body Weak")

st.divider()

# 🎨 Typography Suggestions
typography_suggestions = analyze_typography(image_stats, sections)
final_feedback = generate_design_feedback(overall_score, typography_suggestions)

st.subheader("🎨 Typography & Design Suggestions")

for s in final_feedback:
    st.write("•", s)

st.divider()

st.button("⬅ Back to Upload", on_click=lambda: st.switch_page("app.py"))
