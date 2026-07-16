from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, index=True)

    email = Column(String(255), unique=True, index=True)

    password = Column(String(255))

    conversations = relationship(
        "Conversation", back_populates="user", cascade="all, delete-orphan"
    )
