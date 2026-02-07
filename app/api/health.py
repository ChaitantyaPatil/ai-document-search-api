from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import settings

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    env: str

@router.get("/", response_model=HealthResponse, tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "env": settings.ENV
    }
