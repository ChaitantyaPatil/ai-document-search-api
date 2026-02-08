import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_chunks(
    query_embedding: list,
    chunk_embeddings: list,
    top_k: int = 5
):
    query_vec = np.array(query_embedding).reshape(1, -1)
    chunk_vecs = np.array(chunk_embeddings)

    similarities = cosine_similarity(query_vec, chunk_vecs)[0]

    top_indices = similarities.argsort()[::-1][:top_k]

    return [
        (int(idx), float(similarities[idx]))
        for idx in top_indices
    ]
