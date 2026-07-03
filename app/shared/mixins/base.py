import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class BaseMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class TenantMixin:
    school_id = Column(UUID(as_uuid=True), nullable=False, index=True)


class TimeStampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
