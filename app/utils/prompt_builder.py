def build_prompt(question: str, contexts: list[str]) -> str:
    context_text = "\n\n".join(contexts)

    return f"""
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context_text}

Question:
{question}

Answer:
"""
