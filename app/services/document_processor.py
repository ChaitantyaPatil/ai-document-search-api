import time
from sqlalchemy.orm import Session
from app.models.document import Document
from app.services.text_extractor import extract_text
from app.utils.text_chunker import chunk_text
from app.models.document_chunk import DocumentChunk
from app.services.embedding_service import generate_embedding
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

        # after text extraction
        chunks = chunk_text(doc.extracted_text)

        for chunk in chunks:
            embedding = generate_embedding(chunk)

            db_chunk = DocumentChunk(
                document_id=doc.id,
                content=chunk,
                embedding=embedding
            )
            db.add(db_chunk)

        db.commit()


        # later: text extraction + embeddings
        doc.status = DOCUMENT_STATUS_COMPLETED
        db.commit()

    except Exception:
        if doc:
            doc.status = DOCUMENT_STATUS_FAILED
            db.commit()
