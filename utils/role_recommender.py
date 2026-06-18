def recommend_role(skills):

    skills = set(skills)

    if (
        "Machine Learning" in skills
        and "Python" in skills
    ):
        return "ML Engineer"

    elif (
        "Python" in skills
        and "SQL" in skills
    ):
        return "Data Analyst"

    elif "JavaScript" in skills:
        return "Software Engineer"

    return "General Technology Role"