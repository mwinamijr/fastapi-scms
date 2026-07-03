from app.database.base import Base
from app.database.mixins.base import (
    UUIDMixin,
    TimeStampMixin,
    TenantMixin,
    SoftDeleteMixin,
    AuditMixin,
)


class BaseModel(
    Base, UUIDMixin, AuditMixin, SoftDeleteMixin, TenantMixin, TimeStampMixin
):
    __abstract__ = True
