from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine

from app.routers import chat
from app.routers import auth
from app.routers import conversation

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="LLM Live Chat", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

app.include_router(chat.router, prefix="/chat", tags=["Chat"])

app.include_router(conversation.router, prefix="/conversation", tags=["Conversation"])


@app.get("/")
def root():
    return {"message": "LLM Live Chat API", "version": "1.0.0", "status": "running"}
