from sqlalchemy import Column, ForeignKey
from app.database.models.base_model import BaseModel


class UserRole(BaseModel):
    __tablename__ = "user_roles"

    user_id = Column(ForeignKey("users.id"), nullable=False)
    role_id = Column(ForeignKey("roles.id"), nullable=False)
