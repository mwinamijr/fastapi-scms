from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.modules.identity.repositories.user import UserRepository
from app.modules.identity.schema.user import (
    UserCreateSchema,
    UserResponseSchema,
    UserUpdateSchema,
)

from app.modules.identity.services.user import UserService

router = APIRouter()


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)


@router.post("", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def create_user(
    payload: UserCreateSchema,
    service: UserService = Depends(get_user_service),
):
    return service.create_user(user_data=payload)


@router.get("", response_model=list[UserResponseSchema])
def list_users(
    search: str | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    service: UserService = Depends(get_user_service),
):
    return service.get_all(search=search, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponseSchema)
def get_user(user_id: UUID, service: UserService = Depends(get_user_service)):
    user = service.get(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user


@router.put(
    "/{user_id}",
    response_model=UserResponseSchema,
)
def update_user(
    user_id: UUID,
    payload: UserUpdateSchema,
    service: UserService = Depends(get_user_service),
):
    return service.update(
        user_id=user_id,
        data=payload,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    user_id: UUID,
    service: UserService = Depends(get_user_service),
):
    service.delete(user_id)
