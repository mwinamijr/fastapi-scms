from sqlalchemy.orm import Session
from app.models.user_models import User
from app.utils import verify_password


def authenticate_user(username: str, password: str, db: Session):
    """
    Authenticate a user by verifying their username and password.

    Args:
        username (str): The username provided by the user.
        password (str): The plain-text password provided by the user.
        db (Session): SQLAlchemy database session.

    Returns:
        User: The authenticated user object if successful, None otherwise.
    """
    # Query the user by username
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None  # User not found

    # Verify the provided password with the hashed password
    if not verify_password(password, user.password):
        return None  # Password mismatch

    return user  # Authentication successful
