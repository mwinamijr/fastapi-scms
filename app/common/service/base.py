from typing import Generic, TypeVar, Type
from pydantic import BaseModel

from app.common.repository.base import BaseRepository
from app.database.base import Base

RepoType = TypeVar("RepoType", bound=BaseRepository)
ModelType = TypeVar("ModelType", bound=Base)


class BaseService(Generic[RepoType, ModelType]):

    model: Type[ModelType]

    def __init__(self, repository: RepoType):
        self.repository = repository

    def get(self, id):
        return self.repository.get(id)

    def list(
        self,
        *,
        search: str | None = None,
        filters: dict | None = None,
        skip: int = 0,
        limit: int | None = None,
        order_by: str | None = None,
        order_desc: bool = False,
    ):
        return self.repository.list(
            filters=filters,
            search=search,
            skip=skip,
            limit=limit,
            order_by=order_by,
            order_desc=order_desc,
        )

    def create(self, data: BaseModel, **extra_fields):
        values = data.model_dump()
        values.update(extra_fields)

        obj = self.model(**values)

        return self.repository.create(obj)

    def update(self, id, data: BaseModel):
        obj = self.repository.get(id)

        if obj is None:
            return None

        values = data.model_dump(exclude_unset=True)

        for key, value in values.items():
            setattr(obj, key, value)

        return self.repository.update(obj)

    def delete(self, id):
        obj = self.repository.get(id)

        if obj is None:
            return False

        self.repository.delete(obj)
        return True
