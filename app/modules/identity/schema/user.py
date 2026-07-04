from pydantic import BaseModel

from app.common.schemas.base import (
    BaseResponse,
    BaseCreate,
    BaseUpdate,
    PaginatedResponse,
)


class UserCreateSchema(BaseCreate):
    phone: str
    password: str
    first_name: str
    last_name: str


class UserResponseSchema(BaseResponse):
    phone: str
    first_name: str
    last_name: str


class UserUpdateSchema(BaseUpdate):
    first_name: str | None = None
    last_name: str | None = None
    password: str | None = None


class UserListResponseSchema(PaginatedResponse[UserResponseSchema]):
    users: list[UserResponseSchema]
    total: int
    page: int
    page_size: int


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str


class ResetPasswordSchema(BaseModel):
    phone: str
    new_password: str
