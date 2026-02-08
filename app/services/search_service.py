from app.services.embedding_service import generate_embedding
from app.utils.similarity import find_similar_chunks

def semantic_search(
    query: str,
    chunks: list,
    embeddings: list,
    top_k: int = 5
):
    query_embedding = generate_embedding(query)

    matches = find_similar_chunks(
        query_embedding=query_embedding,
        chunk_embeddings=embeddings,
        top_k=top_k
    )

    results = []
    for idx, score in matches:
        results.append({
            "chunk_id": idx,
            "score": score,
            "text": chunks[idx]
        })

    return results
