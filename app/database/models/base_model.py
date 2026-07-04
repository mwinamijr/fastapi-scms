from app.database.base import Base
from app.database.mixins.base import (
    UUIDMixin,
    TenantMixin,
    TimeStampMixin,
    SoftDeleteMixin,
    AuditMixin,
)


class BaseModel(
    Base,
    UUIDMixin,
    AuditMixin,
    SoftDeleteMixin,
    TimeStampMixin,
):
    __abstract__ = True


class TenantBaseModel(
    TenantMixin,
    BaseModel,
):
    __abstract__ = True
