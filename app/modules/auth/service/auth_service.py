from app.modules.identity.models.user import User
from app.modules.auth.utils.password import verify_password
from app.modules.auth.service.token_service import (
    create_access_token,
    create_refresh_token,
)


class AuthService:
    def __init__(self, db):
        self.db = db

    def authenticate_user(self, phone: str, password: str):
        user = self.db.query(User).filter(User.phone == phone).first()

        if not user:
            return None

        if not verify_password(user.password_hash, password):
            return None

        return user

    def generate_tokens(self, user: User):
        payload = {
            "user_id": str(user.id),
            "school_id": str(user.school_id),
            "user_type": str(user.user_type),
        }

        return {
            "access_token": create_access_token(payload),
            "refresh_token": create_refresh_token(payload),
        }
