import re


def extract_email(text):

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    matches = re.findall(pattern, text)

    if not matches:
        return "Not Found"

    matches = list(dict.fromkeys(matches))

    email = matches[0]

    email = clean_email(email)

    return email
def clean_email(email):

    email = email.strip()

    known_artifacts = [
        "pe",
        "email",
        "mail",
        "envelope"
    ]

    for artifact in known_artifacts:

        if email.startswith(artifact):
            email = email[len(artifact):]

    return email

def extract_phone(text):
    """
    Extract phone number.
    """

    pattern = r'(?:\+?\d[\d\s\-\(\)]{8,}\d)'

    matches = re.findall(pattern, text)

    if not matches:
        return "Not Found"

    return matches[0].strip()


def extract_linkedin(text):
    """
    Extract LinkedIn URL.
    """

    pattern = r'(https?:\/\/)?(www\.)?linkedin\.com\/[^\s]+'

    matches = re.findall(pattern, text)

    if not matches:
        return "Not Found"

    full_match = re.search(
        r'(https?:\/\/)?(www\.)?linkedin\.com\/[^\s]+',
        text
    )

    return full_match.group(0)


def extract_github(text):
    """
    Extract GitHub URL.
    """

    pattern = r'(https?:\/\/)?(www\.)?github\.com\/[^\s]+'

    matches = re.findall(pattern, text)

    if not matches:
        return "Not Found"

    full_match = re.search(
        r'(https?:\/\/)?(www\.)?github\.com\/[^\s]+',
        text
    )

    return full_match.group(0)


def extract_all_info(text):

    return {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "linkedin": extract_linkedin(text),
        "github": extract_github(text)
    }