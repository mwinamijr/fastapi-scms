from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models.user_models import UserRole
from app.schemas.notes_schemas import *
from app.crud import notes_crud

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/subjects", response_model=SubjectResponse)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return notes_crud.create_subject(db, subject)


@router.post("/topics", response_model=TopicResponse)
def create_topic(topic: TopicCreate, db: Session = Depends(get_db)):
    return notes_crud.create_topic(db, topic)


@router.post("/subtopics", response_model=SubTopicResponse)
def create_subtopic(subtopic: SubTopicCreate, db: Session = Depends(get_db)):
    return notes_crud.create_subtopic(db, subtopic)


@router.post("/", response_model=NoteResponse)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if current_user.role != UserRole.teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can create notes",
        )
    return notes_crud.create_note(db, note, current_user.id)


@router.patch("/{note_id}/approve", response_model=NoteResponse)
def approve_note(
    note_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    if current_user.role != UserRole.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can approve notes",
        )
    return notes_crud.approve_note(db, note_id)


@router.delete("/{note_id}")
def delete_note(
    note_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    if current_user.role != UserRole.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Only admins can delete notes"
        )
    return notes_crud.delete_note(db, note_id)
