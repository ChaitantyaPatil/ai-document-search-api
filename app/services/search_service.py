from app.services.embedding_service import generate_embedding
from app.utils.similarity import find_similar_chunks
from app.repositories.chunk_repository import get_all_chunks

def semantic_search(db, query: str, top_k: int = 5):
    records, chunks, embeddings = get_all_chunks(db)

    query_embedding = generate_embedding(query)

    matches = find_similar_chunks(
        query_embedding=query_embedding,
        chunk_embeddings=embeddings,
        top_k=top_k
    )

    results = []
    for idx, score in matches:
        record = records[idx]
        results.append({
            "document_id": record.document_id,
            "chunk_id": record.id,
            "score": score,
            "text": record.chunk_text
        })

    return results
