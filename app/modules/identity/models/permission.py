from sqlalchemy import Column, String
from app.database.models.base_model import BaseModel


class Permission(BaseModel):
    __tablename__ = "permissions"

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
