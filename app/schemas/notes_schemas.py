from pydantic import BaseModel, constr
from typing import List, Optional


class SubjectBase(BaseModel):
    name: constr(max_length=100) = None
    code: constr(max_length=10) = None


class SubjectCreate(SubjectBase):
    pass


class SubjectResponse(SubjectBase):
    id: int

    class Config:
        orm_mode = True


class TopicBase(BaseModel):
    name: constr(max_length=100) = None
    subject_id: int


class TopicCreate(TopicBase):
    pass


class TopicResponse(TopicBase):
    id: int

    class Config:
        orm_mode = True


class SubTopicBase(BaseModel):
    name: constr(max_length=100) = None
    topic_id: int


class SubTopicCreate(SubjectBase):
    pass


class SubTopicResponse(SubjectBase):
    id: int

    class Config:
        orm_mode = True


class NoteBase(BaseModel):
    title: constr(max_length=100) = None
    content: str
    subtopic_id: int


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    title: Optional[str]
    content: Optional[str]
    is_approved: Optional[bool]


class NoteResponse(NoteBase):
    id: int
    is_approved: bool
    created_by_id: int

    class Config:
        orm_mode = True


class IllustrationBase(BaseModel):
    description: constr(max_length=150) = None
    note_id: int


class IllustrationCreate(IllustrationBase):
    pass


class IllustrationResponse(IllustrationBase):
    id: int

    class Config:
        orm_mode = True