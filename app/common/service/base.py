from typing import Generic, TypeVar

from app.common.repository.base import BaseRepository

RepoType = TypeVar("RepoType", bound=BaseRepository)


class BaseService(Generic[RepoType]):
    def __init__(self, repository: RepoType):
        self.repository = repository

    def get(self, id):
        return self.repository.get(id)

    def get_all(self, obj):
        return self.repository.list()

    def create(self, obj):
        return self.repository.create(obj)

    def update(self, obj):
        return self.repository.update(obj)

    def delete(self, obj):
        return self.repository.delete(obj)
