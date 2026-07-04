from sqlalchemy import asc, desc, or_
from sqlalchemy.orm import Session
from typing import Any, Generic, TypeVar, Type
from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: Any) -> ModelType | None:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, obj: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj: ModelType) -> None:
        self.db.delete(obj)
        self.db.commit()

    def exists(self, **filters) -> bool:
        return self.db.query(self.model).filter_by(**filters).first() is not None

    def find_one(self, **filters) -> ModelType | None:
        return self.db.query(self.model).filter_by(**filters).first()

    def find_all(self, **filters) -> list[ModelType]:
        return self.db.query(self.model).filter_by(**filters).all()

    def query(self):
        return self.db.query(self.model)

    # flexible query method to allow for more complex queries
    def list(
        self,
        *,
        filters: dict | None = None,
        search: str | None = None,
        search_fields: list[str] | None = None,
        skip: int = 0,
        limit: int | None = None,
        order_by: Any | None = None,
        order_desc: bool = False,
    ) -> list[ModelType]:
        query = self.query()

        if filters:
            query = query.filter_by(**filters)

        fields = search_fields or getattr(self, "search_fields", [])

        if search and fields:
            conditions = [
                getattr(self.model, field).ilike(f"%{search}%") for field in fields
            ]
            query = query.filter(or_(*conditions))

        if order_by:
            column = getattr(self.model, order_by)

            query = query.order_by(
                desc(column) if order_desc else query.order_by(asc(column))
            )

        if skip is not None:
            query = query.offset(skip)

        if limit is not None:
            query = query.limit(limit)

        return query.all()

    def count(self, filters: dict | None = None) -> int:
        query = self.query()
        if filters:
            query = query.filter_by(**filters)
        return query.count()
