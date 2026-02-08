from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.search_service import semantic_search
from app.utils.prompt_builder import build_prompt
from app.services.llm_service import generate_answer

router = APIRouter(prefix="/ask", tags=["Ask"])

@router.post("/")
async def ask_question(
    question: str,
    db: Session = Depends(get_db)
):
    search_results = semantic_search(db, question, top_k=3)

    contexts = [r["text"] for r in search_results]

    prompt = build_prompt(question, contexts)

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": search_results
    }

