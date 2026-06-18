import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.info_extractor import extract_all_info
from utils.scorer import calculate_score
from utils.role_recommender import recommend_role

st.title("CV Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload your CV",
    type=["pdf"]
)

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    info = extract_all_info(text)
    st.subheader("Candidate Information")
    st.write("Email:", info["email"])
    st.write("Phone:", info["phone"])
    st.write("LinkedIn:", info["linkedin"])
    st.write("GitHub:", info["github"])

    skills = extract_skills(text)
    score = calculate_score(skills)
    role = recommend_role(skills)

    st.subheader("Recommended Role")
    st.success(role)

    st.subheader("Candidate Score")
    st.metric(
        "Overall Score",
        f"{score}/100"
    )
    st.subheader("Skills Found")

    for skill in skills:
        st.write("✅", skill)
        
    st.subheader("Extracted Text")

    st.text_area(
        "",
        text,
        height=400
    )