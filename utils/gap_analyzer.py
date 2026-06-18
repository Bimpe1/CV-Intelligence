def skill_gap_analysis(skills):

    target_skills = [
        "AWS",
        "Kubernetes",
        "FastAPI",
        "CI/CD",
        "MLflow",
        "TensorFlow"
    ]

    missing = []

    for skill in target_skills:

        if skill not in skills:
            missing.append(skill)

    return missing