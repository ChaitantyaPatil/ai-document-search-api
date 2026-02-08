import time
from sqlalchemy.orm import Session
from app.models.document import Document
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

        # simulate heavy processing
        time.sleep(5)

        # later: text extraction + embeddings
        doc.status = DOCUMENT_STATUS_COMPLETED
        db.commit()

    except Exception:
        if doc:
            doc.status = DOCUMENT_STATUS_FAILED
            db.commit()
