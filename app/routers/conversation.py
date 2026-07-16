from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.conversation import Conversation

router = APIRouter()


# Get all conversations
@router.get("/")
def get_conversations(db: Session = Depends(get_db)):
    conversations = db.query(Conversation).order_by(Conversation.created_at).all()

    return conversations


# Get conversation by session id
@router.get("/{session_id}")
def get_session(session_id: str, db: Session = Depends(get_db)):
    messages = (
        db.query(Conversation)
        .filter(Conversation.session_id == session_id)
        .order_by(Conversation.created_at)
        .all()
    )

    return messages


# Save a message
@router.post("/")
def save_message(
    session_id: str,
    role: str,
    message: str,
    db: Session = Depends(get_db),
):
    chat = Conversation(
        session_id=session_id,
        role=role,
        message=message,
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return {
        "success": True,
        "data": chat,
    }


# Delete a conversation session
@router.delete("/{session_id}")
def delete_session(session_id: str, db: Session = Depends(get_db)):
    rows = db.query(Conversation).filter(Conversation.session_id == session_id).all()

    if not rows:
        raise HTTPException(status_code=404, detail="Conversation not found")

    for row in rows:
        db.delete(row)

    db.commit()

    return {"success": True, "message": "Conversation deleted"}


# Delete all conversations
@router.delete("/")
def delete_all(db: Session = Depends(get_db)):
    db.query(Conversation).delete()
    db.commit()

    return {"success": True, "message": "All conversations deleted"}
