from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.document import Document

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
