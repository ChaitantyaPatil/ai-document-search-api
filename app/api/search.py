from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.search import SearchRequest, SearchResult
from app.services.search_service import semantic_search

router = APIRouter(prefix="/search", tags=["Search"])

@router.post("/", response_model=list[SearchResult])
async def search_docs(
    payload: SearchRequest,
    db: Session = Depends(get_db)
):
    return semantic_search(
        db=db,
        query=payload.query,
        top_k=payload.top_k
    )
