from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Document Search API")

class HealthResponse(BaseModel):
    status: str

@app.get("/", response_model=HealthResponse)
async def health_check():
    return {"status": "ok"}

@app.get("/hello/{name}")
async def say_hello(name: str, age: int = 0):
    return {
        "message": f"Hello {name}",
        "age": age
    }
