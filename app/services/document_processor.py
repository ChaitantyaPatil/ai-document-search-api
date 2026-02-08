import time
from sqlalchemy.orm import Session
from app.models.document import Document
from app.services.text_extractor import extract_text
from app.core.constants import (
    DOCUMENT_STATUS_PROCESSING,
    DOCUMENT_STATUS_COMPLETED,
    DOCUMENT_STATUS_FAILED
)

def process_document(doc_id: int, db: Session):
    try:
        # mark as processing
        doc = db.query(Document).filter(Document.id == doc_id).first()
        if not doc:
            return

        doc.status = DOCUMENT_STATUS_PROCESSING
        db.commit()

        # 🔥 TEXT EXTRACTION
        text = extract_text(doc.file_path)
        doc.extracted_text = text

        # later: text extraction + embeddings
        doc.status = DOCUMENT_STATUS_COMPLETED
        db.commit()

    except Exception:
        if doc:
            doc.status = DOCUMENT_STATUS_FAILED
            db.commit()
