"""
Resume Parser Module
Extracts plain text and basic contact/education metadata from PDF, DOCX, and TXT files.
"""

import io
import re
from typing import Tuple, Dict, Any

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF file bytes using pdfplumber."""
    try:
        import pdfplumber
        text_parts = []
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        return "\n".join(text_parts)
    except Exception as e:
        # Fallback basic binary string extraction if pdfplumber fails
        try:
            raw = file_bytes.decode('latin-1', errors='ignore')
            matches = re.findall(r'[A-Za-z0-9 ,.\-_/@#+]{4,}', raw)
            return "\n".join(matches)
        except Exception:
            return f"Error extracting PDF: {str(e)}"

def extract_text_from_docx(file_bytes: bytes) -> str:
    """Extract text from DOCX file bytes using python-docx."""
    try:
        import docx
        doc = docx.Document(io.BytesIO(file_bytes))
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text.strip())
        for table in doc.tables:
            for row in table.rows:
                row_text = [cell.text.strip() for cell in row.cells if cell.text.strip()]
                if row_text:
                    full_text.append(" | ".join(row_text))
        return "\n".join(full_text)
    except Exception as e:
        return f"Error extracting DOCX: {str(e)}"

def extract_text_from_file(file_obj, filename: str) -> str:
    """Read uploaded file (Streamlit UploadedFile or file-like) and extract text."""
    if hasattr(file_obj, "read"):
        file_bytes = file_obj.read()
    elif isinstance(file_obj, bytes):
        file_bytes = file_obj
    elif isinstance(file_obj, str):
        with open(file_obj, "rb") as f:
            file_bytes = f.read()
    else:
        return ""

    ext = filename.lower().split('.')[-1]
    if ext == 'pdf':
        return extract_text_from_pdf(file_bytes)
    elif ext in ['docx', 'doc']:
        return extract_text_from_docx(file_bytes)
    else:
        try:
            return file_bytes.decode('utf-8', errors='ignore')
        except Exception:
            return file_bytes.decode('latin-1', errors='ignore')

def extract_candidate_metadata(text: str) -> Dict[str, Any]:
    """Extract candidate email, phone, and guessed name from resume text."""
    metadata = {
        "name": "Candidate",
        "email": "Not Found",
        "phone": "Not Found",
        "degree": "B.E. / B.Tech (AIML / CSE)"
    }
    
    # Email regex
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    if email_match:
        metadata["email"] = email_match.group(0)

    # Phone regex (Indian/international 10-12 digits)
    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    if phone_match:
        metadata["phone"] = phone_match.group(0)

    # Candidate Name heuristic (first non-empty line with letters)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    for line in lines[:5]:
        if len(line.split()) in [2, 3, 4] and not re.search(r'resume|curriculum|vitae|page|contact|email|phone', line, re.I):
            clean_name = re.sub(r'[^a-zA-Z\s\.]', '', line).strip()
            if len(clean_name) > 3:
                metadata["name"] = clean_name
                break

    return metadata
