from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.models.user_models import User
from app.database import get_db
from app.config import settings
from sqlalchemy.orm import Session
from app.models.user_models import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
ALGORITHM = "HS256"


def decode_access_token(token: str):
    """
    Decodes a JWT and extracts the payload, converting role back to UserRole enum.
    """
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")
    role = UserRole(payload.get("role"))  # Convert string back to UserRole enum
    return {"username": username, "role": role}


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        # Decode the token
        payload = decode_access_token(token)
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Fetch user from database
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def is_admin_or_self(
    current_user: User = Depends(get_current_user), user_id: int = None
):
    if current_user.role == "admin" or current_user.id == user_id:
        return current_user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access denied.",
    )


def is_system_not_initialized(db: Session = Depends(get_db)):
    """
    Ensures the initialization endpoint is only accessible when no admin exists.
    """
    existing_admin = db.query(User).filter(User.role == "admin").first()
    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="System is already initialized. Admin user exists.",
        )
