from pydantic import BaseModel

from app.common.schemas.base import (
    BaseResponse,
    BaseCreate,
    BaseUpdate,
)


class PermissionCreateSchema(BaseCreate):
    name: str
    description: str | None = None


class PermissionResponseSchema(BaseResponse):
    id: int
    name: str
    description: str | None = None


class PermissionUpdateSchema(BaseUpdate):
    name: str | None = None
    description: str | None = None


class AssignPermissionSchema(BaseModel):
    role_id: int
    permission_id: int
