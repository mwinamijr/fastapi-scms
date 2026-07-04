from sqlalchemy import Column, String
from app.database.models.base_model import TenantBaseModel


class Role(TenantBaseModel):
    __tablename__ = "roles"

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
