from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_service import save_uploaded_file
from pydantic import BaseModel


router = APIRouter(prefix="/upload", tags=["Documents"])

class UploadResponse(BaseModel):
    filename: str
    status: str
    path: str


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_path = await save_uploaded_file(file)
        return {
            "filename": file.filename,
            "status": "uploaded",
            "path": file_path
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
