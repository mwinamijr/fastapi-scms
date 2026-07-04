from sqlalchemy import Boolean, Column, String
from app.database.models.base_model import TenantBaseModel


class User(TenantBaseModel):
    __tablename__ = "users"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    usernane = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    phone = Column(String, unique=True, index=True, nullable=False)

    password_hash = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    user_type = Column(String, nullable=False)  # e.g: admin, teacher, staff
