import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.info_extractor import extract_all_info
from utils.scorer import calculate_score
from utils.role_recommender import recommend_role
from utils.matcher import calculate_match_score

st.title("CV Intelligence Platform")
st.subheader("Job Description")

job_description = st.text_area(
    "Paste the Job Description",
    height=250
)
uploaded_file = st.file_uploader(
    "Upload your CV",
    type=["pdf"]
)
# job_description = st.text_area(
#     "Paste Job Description",
#     height=250,
#     placeholder="Paste an ML Engineer or Software Engineer job description here..."
# )
if uploaded_file:
    try:
        text = extract_text_from_pdf(uploaded_file)

    except Exception as e:
        st.error(
        """
        Unable to process this PDF.

        Possible reasons:\n
        • The PDF is corrupted.\n
        • The PDF is password protected.\n
        • The PDF was exported incorrectly.

        Please try another PDF.
        """
    )
        st.stop()

    info = extract_all_info(text)    # match_score = None

    # if job_description:
    #     match_score = calculate_match_score(
    #         text,
    #         job_description
    #     )
    match_score = None

    if job_description.strip():
        with st.spinner("Analyzing CV against job description..."):
            match_score = calculate_match_score(
                text,
                job_description
            )
    st.subheader("Candidate Information")
    st.write("Name:", info["name"])
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
    if score >= 80:
        st.success("Strong Candidate")
    elif score >= 60:
        st.warning("Moderate Candidate")
    else:
        st.error("Needs Improvement")

    if match_score is not None:

        st.subheader("Semantic Job Match")
        st.metric(
            "Match Score",
            f"{match_score}%"
        )
        
    st.subheader("Skills Found")
    for skill in skills:
        st.write("✅", skill)
        
    with st.expander("View Extracted CV Text"):
        st.text_area("", text, height=400)
  