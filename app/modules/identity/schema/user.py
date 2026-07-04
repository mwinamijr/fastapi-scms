import re
from pydantic import BaseModel, EmailStr, constr, field_validator
from typing import Optional
from uuid import UUID

from app.common.schemas.base import (
    BaseResponse,
    BaseCreate,
    BaseUpdate,
    PaginatedResponse,
)


class PersonBaseSchema:
    first_name: str
    last_name: str
    phone: str
    email: EmailStr | None = None


class UserBaseSchema:
    phone: str
    email: Optional[EmailStr] = None
    first_name: str
    last_name: str
    school_id: UUID
    username: str
    user_type: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        pattern = r"^\+255\d{9}$"

        if not re.match(pattern, value):
            raise ValueError(
                "Phone number must be in international format (+255XXXXXXXXX)."
            )

        return value


class UserResponseSchema(BaseResponse, UserBaseSchema):
    is_active: bool
    is_verified: bool


class UserCreateSchema(BaseCreate, UserBaseSchema):
    password: str


class UserUpdateSchema(BaseUpdate):
    school_id: UUID | None = None
    username: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None
    user_type: str | None = None

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if value is None:
            return value

        pattern = r"^\+255\d{9}$"

        if not re.match(pattern, value):
            raise ValueError(
                "Phone number must be in international format (+255XXXXXXXXX)."
            )

        return value


class UserListResponseSchema(PaginatedResponse[UserResponseSchema]):
    pass


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str


class ResetPasswordSchema(BaseModel):
    phone: str
    new_password: str
