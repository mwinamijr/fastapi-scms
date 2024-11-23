import enum
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, text
from app.models.base import BaseModel


# Enum for roles
class UserRole(enum.Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    role = Column(Enum(UserRole), nullable=False)  # "admin", "teacher", "student"
    hashed_password = Column(String(128), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
