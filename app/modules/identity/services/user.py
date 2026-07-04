from app.common.service.base import BaseService
from app.modules.identity.repositories.user import UserRepository


class UserService(BaseService[UserRepository]):

    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    def create_user(self, user_data):
        if self.repository.get_user_by_phone(user_data.phone):
            raise ValueError("User with this phone number already exists.")

        return self.repository.create(user_data)

    def list_users(self, search: str | None, skip: int, limit: int):
        return self.repository.list(search=search, skip=skip, limit=limit)

    def update_user(self, user_id: int, user_data):
        user = self.repository.get(user_id)
        if not user:
            raise ValueError("User not found.")

        values = user_data.model_dump(exclude_unset=True)

        for key, value in values.items():
            setattr(user, key, value)

        return self.repository.update(user)
