from io import BytesIO

import fitz  # PyMuPDF
from pypdf import PdfReader
from pypdf.errors import PdfReadError


def extract_text_pymupdf(pdf_bytes):
    """Extract text using PyMuPDF."""

    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text.strip()


def extract_text_pypdf(pdf_bytes):
    """Extracting text using pypdf."""

    reader = PdfReader(BytesIO(pdf_bytes))

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def extract_text_from_pdf(pdf_file):
    """
    Production-ready PDF parser.

    Strategy:
    1. Try PyMuPDF
    2. Fallback to pypdf
    3. Raise friendly error
    """

    pdf_file.seek(0)
    pdf_bytes = pdf_file.read()

    # First attempt: PyMuPDF
    try:
        return extract_text_pymupdf(pdf_bytes)

    except Exception:
        pass

    # Second attempt: pypdf
    try:
        return extract_text_pypdf(pdf_bytes)

    except PdfReadError:
        pass

    raise Exception(
        "Unable to read this PDF. It may be corrupted, encrypted, or unsupported."
    )