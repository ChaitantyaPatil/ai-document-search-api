import requests
from app.core.config import settings
from openai import OpenAI


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=settings.HF_API_TOKEN,
)

def generate_answer(prompt: str) -> str:
    completion = client.chat.completions.create(
        model=settings.HF_MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Answer using only the provided context."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=300,
    )

    return completion.choices[0].message.content