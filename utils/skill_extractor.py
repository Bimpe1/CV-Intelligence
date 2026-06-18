import re

SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "Git",
    "FastAPI",
    "Flask",
    "Django",
    "Power BI",
    "Tableau",
    "Linux",
    "MongoDB",
    "PostgreSQL"
]


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return sorted(found_skills)