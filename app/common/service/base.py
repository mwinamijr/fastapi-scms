from typing import Generic, TypeVar
from sqlalchemy.orm import Session

from app.common.repository.base import BaseRepository

RepoType = TypeVar("RepoType", bound=BaseRepository)


class BaseService(Generic[RepoType]):
    def __init__(self, repository: RepoType):
        self.repository = repository
