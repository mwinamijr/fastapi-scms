from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import create_access_token, verify_password
from app.config import settings
from app.crud.user_crud import get_user_by_username, create_user
from app.dependencies import get_current_user, is_system_not_initialized
from app.schemas.user_schemas import Token, UserLogin, UserCreate, UserResponse
from app.models.user_models import User
from app.utils import hash_password

router = APIRouter()


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = get_user_by_username(db, username=form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserLogin)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user


@router.post(
    "/initialize",
    response_model=UserResponse,
    tags=["Initialization"],
    summary="Initialize the system",
    description="Creates the first admin user in the system. Disabled once an admin user exists.",
)
def initialize_system(
    admin_data: UserCreate,
    secret_key: str,
    db: Session = Depends(get_db),
    system_not_initialized: None = Depends(is_system_not_initialized),
):
    """
    Create the first admin user. This endpoint is disabled once an admin user exists.
    """
    # Verify the secret key
    if secret_key != settings.INITIALIZE_SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid secret key.",
        )

    # Hash the password and create the admin user
    admin_data.password = hash_password(admin_data.password)
    admin_user = create_user(db, admin_data)

    return admin_user
