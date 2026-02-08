from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.document import Document
from app.models.document_chunk import DocumentChunk

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("/{doc_id}")
def get_document_status(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "id": doc.id,
        "filename": doc.filename,
        "status": doc.status,
        "created_at": doc.created_at
    }

@router.get("/{doc_id}/text")
def get_extracted_text(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    if not doc.extracted_text:
        return {"message": "Text not yet extracted"}

    return {
        "id": doc.id,
        "filename": doc.filename,
        "text_preview": doc.extracted_text[:1000]
    }

@router.get("/{doc_id}/chunks")
def get_document_chunks(doc_id: int, db: Session = Depends(get_db)):
    chunks = db.query(DocumentChunk).filter(
        DocumentChunk.document_id == doc_id
    ).all()

    return {
        "document_id": doc_id,
        "total_chunks": len(chunks),
        "sample_chunk": chunks[0].content[:500] if chunks else None
    }
