from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def calculate_match_score(
    cv_text,
    job_text
):

    cv_embedding = model.encode(
        cv_text,
        convert_to_tensor=True
    )

    job_embedding = model.encode(
        job_text,
        convert_to_tensor=True
    )

    similarity = cos_sim(
        cv_embedding,
        job_embedding
    )

    return round(
        float(similarity[0][0]) * 100,
        2
    )