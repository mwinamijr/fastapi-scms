from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseResponse(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BaseCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")


class BaseUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Pagination(BaseModel):
    page: int = 1
    page_size: int = 20


class PaginatedResponse(BaseModel, Generic[T]):
    total: int
    page: int
    page_size: int
    items: list[T]
