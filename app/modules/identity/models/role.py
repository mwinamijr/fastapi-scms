from sqlalchemy import Column, String, ForeignKey
from app.database.models.base_model import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    school_id = Column(ForeignKey("schools.id"), nullable=False, index=True)

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
