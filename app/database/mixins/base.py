import uuid
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class UUIDMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class TimeStampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class TenantMixin:
    school_id = Column(UUID(as_uuid=True), nullable=False, index=True)


class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False)


class AuditMixin:
    created_by = Column(UUID(as_uuid=True), nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    created_ip = Column(String, nullable=True)
    updated_ip = Column(String, nullable=True)
