from PyPDF2 import PdfReader
from docx import Document as DocxDocument

def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    return "\n".join(text)


def extract_text_from_docx(file_path: str) -> str:
    doc = DocxDocument(file_path)
    text = [para.text for para in doc.paragraphs if para.text.strip()]
    return "\n".join(text)


def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

import os

def extract_text(file_path: str) -> str:
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif extension == ".docx":
        return extract_text_from_docx(file_path)
    elif extension == ".txt":
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file format for text extraction")
