from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.notes_models import Subject, Topic, SubTopic, Note
from app.schemas.notes_schemas import SubjectOut, TopicOut, SubtopicOut, NoteOut
from typing import List

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


# Get all subjects
@router.get("/subjects", response_model=List[SubjectOut])
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    return subjects


# Get topics for a specific subject
@router.get("/subjects/{subject_id}/topics", response_model=List[TopicOut])
def get_topics(subject_id: int, db: Session = Depends(get_db)):
    topics = db.query(Topic).filter(Topic.subject_id == subject_id).all()
    if not topics:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No topics found for this subject",
        )
    return topics


# Get subtopics for a specific topic
@router.get("/topics/{topic_id}/subtopics", response_model=List[SubtopicOut])
def get_subtopics(topic_id: int, db: Session = Depends(get_db)):
    subtopics = db.query(SubTopic).filter(SubTopic.topic_id == topic_id).all()
    if not subtopics:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No subtopics found for this topic",
        )
    return subtopics


# Get approved notes for a specific subtopic
@router.get("/subtopics/{subtopic_id}/notes", response_model=List[NoteOut])
def get_notes(subtopic_id: int, db: Session = Depends(get_db)):
    notes = (
        db.query(Note)
        .filter(Note.subtopic_id == subtopic_id, Note.is_approved == True)
        .all()
    )
    if not notes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No approved notes found for this subtopic",
        )
    return notes
