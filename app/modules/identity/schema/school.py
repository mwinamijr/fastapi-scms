import re
from pydantic import EmailStr, field_validator
from typing import Optional, Literal

from app.common.schemas.base import (
    BaseResponse,
    BaseCreate,
    BaseUpdate,
)


class SchoolBaseSchema:
    name: str
    phone: str
    code: str
    address: str | None = None
    ownership: Literal["private", "government"]
    school_email: Optional[EmailStr] = None
    mission: str | None = None
    vission: str | None = None
    school_logo: str | None = None

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        pattern = r"^\+255\d{9}$"

        if not re.match(pattern, value):
            raise ValueError(
                "Phone number must be in international format (+255XXXXXXXXX)."
            )

        return value


class SchoolCreateSchema(BaseCreate, SchoolBaseSchema):
    pass


class SchoolUpdateSchema(BaseUpdate):
    name: str | None = None
    address: str | None = None
    phone: str | None = None
    code: str | None = None
    address: str | None = None
    ownership: str | None = None
    school_email: EmailStr = None
    mission: str | None = None
    vission: str | None = None
    school_logo: str | None = None

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        pattern = r"^\+255\d{9}$"

        if not re.match(pattern, value):
            raise ValueError(
                "Phone number must be in international format (+255XXXXXXXXX)."
            )

        return value


class SchoolResponseSchema(BaseResponse, SchoolBaseSchema):
    is_active: bool
