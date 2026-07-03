from sqlalchemy import Column, ForeignKey
from app.database.models.base_model import BaseModel


class RolePermission(BaseModel):
    __tablename__ = "role_permissions"

    role_id = Column(ForeignKey("roles.id"), nullable=False)
    permission_id = Column(ForeignKey("roles.id"), nullable=False)
