from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.modules.identity.repositories.school import SchoolRepository
from app.modules.identity.schema.school import (
    SchoolCreateSchema,
    SchoolResponseSchema,
    SchoolUpdateSchema,
)

from app.modules.identity.services.school import SchoolService

router = APIRouter()


def get_school_service(db: Session = Depends(get_db)) -> SchoolService:
    repository = SchoolRepository(db)
    return SchoolService(repository)


@router.post(
    "", response_model=SchoolResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_school(
    payload: SchoolCreateSchema,
    service: SchoolService = Depends(get_school_service),
):
    return service.create(payload)


@router.get("", response_model=list[SchoolResponseSchema])
def list_schools(
    search: str | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    service: SchoolService = Depends(get_school_service),
):
    return service.list(search=search, skip=skip, limit=limit)


@router.get("/{school_id}", response_model=SchoolResponseSchema)
def get_school(school_id: UUID, service: SchoolService = Depends(get_school_service)):
    school = service.get(school_id)
    if school is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="School not found"
        )

    return school


@router.put(
    "/{school_id}",
    response_model=SchoolResponseSchema,
)
def update_school(
    school_id: UUID,
    payload: SchoolUpdateSchema,
    service: SchoolService = Depends(get_school_service),
):
    return service.update(
        school_id,
        payload,
    )


@router.delete(
    "/{school_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_school(
    school_id: UUID,
    service: SchoolService = Depends(get_school_service),
):
    service.delete(school_id)
