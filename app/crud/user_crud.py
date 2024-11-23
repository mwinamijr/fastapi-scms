from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query
from fastapi import HTTPException
from app.models.user_models import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.utils import hash_password


def create_user(db: Session, user: UserCreate):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="username already exists")
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registerd")

    new_user = User(
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hash_password(user.password),
        role=user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a paginated list of users from the database.

    Args:
        db (Session): The database session.
        skip (int): Number of records to skip (for pagination).
        limit (int): Maximum number of records to return.

    Returns:
        List[User]: A list of user objects.
    """
    query: Query = db.query(User)
    return query.offset(skip).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# Update user information
def update_user(db: Session, user_id: int, user: UserUpdate):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    for field, value in user.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user


# Delete user
def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()

    return {"message": " User deleted successfully"}
