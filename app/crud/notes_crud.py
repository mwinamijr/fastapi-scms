from sqlalchemy.orm import Session
from app.models.notes_models import Subject, Topic, SubTopic, Note, Illustration
from app.schemas.notes_schemas import *


def create_subject(db: Session, subject: SubjectCreate):
    new_subject = Subject(**subject.dict())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject


def create_topic(db: Session, topic: TopicCreate):
    new_topic = Topic(**topic.dict())
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic


def create_subtopic(db: Session, subtopic: SubTopicCreate):
    new_subtopic = SubTopic(**subtopic.dict())
    db.add(new_subtopic)
    db.commit()
    db.refresh(new_subtopic)
    return new_subtopic


def create_note(db: Session, note: NoteCreate, created_by_id: int):
    new_note = Note(**note.dict(), created_by_id=created_by_id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


def approve_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        note.is_approved = True
        db.commit()
        db.refresh(note)
    return note


def delete_note(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    return note


def create_illustration(db: Session, illustration: IllustrationCreate):
    new_illustration = Illustration(**illustration.dict())
    db.add(new_illustration)
    db.commit()
    db.refresh(new_illustration)
    return new_illustration


def update_illustration(
    db: Session, illustration_id: int, new_illustration: IllustrationUpdate
):
    illustration = (
        db.query(Illustration).filter(Illustration.id == illustration_id).first()
    )
    if illustration:
        if new_illustration.description is not None:
            illustration.description = new_illustration.description
        if new_illustration.image is not None:
            illustration.image = new_illustration.image
        db.commit()
        db.refresh(illustration)
    return illustration
