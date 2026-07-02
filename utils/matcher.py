from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
import streamlit as st


@st.cache_resource
def load_model():
    """
    Load the Sentence Transformer model only once.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


def calculate_match_score(cv_text, job_description):
    """
    Compare CV and Job Description semantically.
    """

    cv_embedding = model.encode(
        cv_text,
        convert_to_tensor=True
    )

    job_embedding = model.encode(
        job_description,
        convert_to_tensor=True
    )

    similarity = cos_sim(
        cv_embedding,
        job_embedding
    )

    return round(float(similarity[0][0]) * 100, 2)