from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.services.file_service import save_uploaded_file
from app.services.document_processor import process_document
from app.core.database import get_db
from app.models.document import Document
from app.core.constants import DOCUMENT_STATUS_UPLOADED

router = APIRouter(prefix="/upload", tags=["Documents"])

@router.post("/")
async def upload_document(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        file_path = await save_uploaded_file(file)

        doc = Document(
            filename=file.filename,
            file_path=file_path,
            status=DOCUMENT_STATUS_UPLOADED
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)

        background_tasks.add_task(process_document, doc.id, db)

        return {
            "id": doc.id,
            "filename": doc.filename,
            "status": doc.status
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
