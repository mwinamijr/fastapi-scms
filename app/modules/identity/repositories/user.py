from app.common.repository.base import BaseRepository
from app.modules.identity.models.user import User


class UserRepository(BaseRepository[User]):

    search_fields = ["first_name", "last_name", "email", "phone"]

    def __init__(self, db):
        super().__init__(User, db)

    def get_user_by_phone(self, phone: str):
        return self.db.query(User).filter(User.phone == phone).first()

    def activate_user(self, user: User):
        user.is_active = True
        self.db.commit()
        self.db.refresh(user)
        return user

    def deactivate_user(self, user: User):
        user.is_active = False
        self.db.commit()
        self.db.refresh(user)
        return user

    def assign_role_to_user(self, user: User, role_id: int):
        user.role_id = role_id
        self.db.commit()
        self.db.refresh(user)
        return user

    def remove_role_from_user(self, user: User):
        user.role_id = None
        self.db.commit()
        self.db.refresh(user)
        return user

    def change_user_password(self, user: User, new_password: str):
        user.password = new_password
        self.db.commit()
        self.db.refresh(user)
        return user

    def reset_user_password(self, user: User, new_password: str):
        user.password = new_password
        self.db.commit()
        self.db.refresh(user)
        return user
