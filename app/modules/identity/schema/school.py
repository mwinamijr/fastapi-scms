from app.common.schemas.base import (
    BaseResponse,
    BaseCreate,
    BaseUpdate,
)


class SchoolCreateSchema(BaseCreate):
    name: str
    address: str | None = None
    phone: str | None = None


class SchoolUpdateSchema(BaseUpdate):
    name: str | None = None
    address: str | None = None
    phone: str | None = None


class SchoolResponseSchema(BaseResponse):
    name: str
    address: str | None = None
    phone: str | None = None
