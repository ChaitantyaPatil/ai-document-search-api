from fastapi import APIRouter
from app.schemas.search import SearchRequest, SearchResult
from app.services.search_service import semantic_search

router = APIRouter(prefix="/search", tags=["Search"])

# TEMP: Replace with DB later
DUMMY_CHUNKS = [
    "FastAPI is a modern web framework",
    "Embeddings capture semantic meaning",
    "Python is widely used in AI",
]

DUMMY_EMBEDDINGS = [
    [0.01] * 384,
    [0.02] * 384,
    [0.03] * 384,
]

@router.post("/", response_model=list[SearchResult])
async def search_docs(payload: SearchRequest):
    results = semantic_search(
        query=payload.query,
        chunks=DUMMY_CHUNKS,
        embeddings=DUMMY_EMBEDDINGS,
        top_k=payload.top_k
    )

    return [
        {
            "document_id": 1,
            "chunk_id": r["chunk_id"],
            "score": r["score"],
            "text": r["text"]
        }
        for r in results
    ]
