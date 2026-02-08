import json
from sqlalchemy.orm import Session
from app.models.document_chunk import DocumentChunk

def get_all_chunks(db: Session):
    records = db.query(DocumentChunk).all()

    chunks = []
    embeddings = []

    for r in records:
        chunks.append(r.content)
        embeddings.append(r.embedding)

    return records, chunks, embeddings
