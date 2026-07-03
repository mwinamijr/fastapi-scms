from sqlalchemy import Boolean, Column, String
from app.database.models.base_model import BaseModel


class School(BaseModel):
    __tablename__ = "schools"

    name = Column(String, nullable=False)
    code = Column(String, unique=True, index=True)

    is_active = Column(Boolean, default=True)
