import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI App")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    ENV: str = os.getenv("ENV", "dev")
    HF_API_TOKEN = os.getenv("HF_API_TOKEN")
    HF_MODEL_NAME = os.getenv("HF_MODEL_NAME")

settings = Settings()
