def calculate_score(skills):

    score = 0

    weights = {
        "Python": 15,
        "SQL": 10,
        "Git": 10,
        "Docker": 10,
        "AWS": 15,
        "Machine Learning": 15,
        "PyTorch": 10,
        "TensorFlow": 10,
        "FastAPI": 5
    }

    for skill in skills:

        if skill in weights:
            score += weights[skill]

    return min(score, 100)