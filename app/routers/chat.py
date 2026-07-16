from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_service import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/")
async def chat(req: ChatRequest):

    answer = ask_gemini(req.message)

    return {"reply": answer}
