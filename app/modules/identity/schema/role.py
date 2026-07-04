from pydantic import BaseModel

from app.common.schemas.base import (
    BaseResponse,
    BaseCreate,
    BaseUpdate,
)


class RoleCreateSchema(BaseCreate):
    name: str
    description: str | None = None


class RoleResponseSchema(BaseResponse):
    name: str
    description: str | None = None


class RoleUpdateSchema(BaseUpdate):
    name: str | None = None
    description: str | None = None


class AssignRoleSchema(BaseModel):
    user_id: int
    role_id: int
