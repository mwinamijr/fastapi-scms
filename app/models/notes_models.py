from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

# from app.models.user_models import User


class Subject(BaseModel):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    code = Column(String(10), unique=True, nullable=False)

    topics = relationship("Topic", back_populates="subjects")


class Topic(BaseModel):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.id"))

    subject = relationship("Subject", back_populates="topics")
    subtopics = relationship("SubTopic", back_populates="topic")


class SubTopic(BaseModel):
    __tablename__ = "subtopics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id"))

    topic = relationship("Topic", back_populates="subtopics")
    notes = relationship("Note", back_populates="subtopic")


class Note(BaseModel):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullble=False)
    is_approved = Column(Boolean, default=False)
    subtopic_id = Column(Integer, ForeignKey("subtopic.id"))
    created_by_id = Column(Integer, ForeignKey=("users.id"))

    subtopic = relationship("Subtopic", back_populates="notes")
    created_by = relationship("User", back_populates="notes")
    illustrations = relationship("Illustration", back_populates="note")


class Illustration(BaseModel):
    __tablename__ = "illustrations"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(150), nullable=True)
    note_id = Column(Integer, ForeignKey("notes.id"))

    note = relationship("Note", back_populates="illustrations")
