from app.common.repository.base import BaseRepository
from app.modules.identity.models.role import Role


class RoleRepository(BaseRepository[Role]):

    def __init__(self, db):
        super().__init__(db, Role)

    def assign_permission_to_role(self, role: Role, permission_id: int):
        if permission_id not in role.permissions:
            role.permissions.append(permission_id)
            self.db.commit()
            self.db.refresh(role)
        return role

    def remove_permission_from_role(self, role: Role, permission_id: int):
        if permission_id in role.permissions:
            role.permissions.remove(permission_id)
            self.db.commit()
            self.db.refresh(role)
        return role
