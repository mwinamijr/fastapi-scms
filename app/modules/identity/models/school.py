from sqlalchemy import Boolean, Column, String
from app.database.models.base_model import BaseModel


class School(BaseModel):
    __tablename__ = "schools"

    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    code = Column(String, unique=True, index=True)
    school_email = Column(String, nullable=True)
    address = Column(String, nullable=True)
    ownership = Column(String, nullable=True)
    mission = Column(String, nullable=True)
    vission = Column(String, nullable=True)

    school_logo = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
