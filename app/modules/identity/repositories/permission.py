from app.common.repository.base import BaseRepository
from app.modules.identity.models.permission import Permission


class PermissionRepository(BaseRepository[Permission]):

    def __init__(self, db):
        super().__init__(db, Permission)
