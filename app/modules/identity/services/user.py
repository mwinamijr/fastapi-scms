from app.common.service.base import BaseService
from app.modules.identity.repositories.user import UserRepository


class UserService(BaseService[UserRepository]):

    def __init__(self, repository: UserRepository):
        super().__init__(repository)

    def create_user(self, user_data):
        if self.repository.get_user_by_phone(user_data.phone):
            raise ValueError("User with this phone number already exists.")

        return self.repository.create(user_data)
