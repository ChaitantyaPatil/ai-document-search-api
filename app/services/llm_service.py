import requests
from app.core.config import HF_API_TOKEN, HF_MODEL_NAME

HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_NAME}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def generate_answer(prompt: str) -> str:
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.3
        }
    }

    response = requests.post(
        HF_API_URL,
        headers=HEADERS,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        raise Exception(f"HF API Error: {response.text}")

    result = response.json()

    # flan-t5 returns generated_text
    return result[0]["generated_text"]
