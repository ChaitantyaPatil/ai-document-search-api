from app.core.database import engine
from app.models import document, document_chunk
from app.core.database import Base

def init_db():
    Base.metadata.create_all(bind=engine)
