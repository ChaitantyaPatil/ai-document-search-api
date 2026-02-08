from fastapi import FastAPI
from app.core.config import settings
from app.api import health, upload
from app.core.init_db import init_db
from app.api import health, upload, documents

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(health.router)
app.include_router(upload.router)
app.include_router(documents.router)

