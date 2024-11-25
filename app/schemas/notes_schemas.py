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
        from_attributes = True


class TopicBase(BaseModel):
    name: constr(max_length=100) = None
    subject_id: int


class TopicCreate(TopicBase):
    pass


class TopicResponse(TopicBase):
    id: int

    class Config:
        from_attributes = True


class SubTopicBase(BaseModel):
    name: constr(max_length=100) = None
    topic_id: int


class SubTopicCreate(SubjectBase):
    pass


class SubTopicResponse(SubjectBase):
    id: int

    class Config:
        from_attributes = True


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
        from_attributes = True


class IllustrationBase(BaseModel):
    description: constr(max_length=150) = None
    note_id: int
    image: Optional[str] = None  # Optional field for image


class IllustrationCreate(IllustrationBase):
    pass


class IllustrationUpdate(IllustrationBase):
    id: int
    description: Optional[str] = None
    image: Optional[str] = None


class IllustrationResponse(IllustrationBase):
    id: int

    class Config:
        from_attributes = True


class SubjectOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TopicOut(BaseModel):
    id: int
    name: str
    subject_id: int

    class Config:
        from_attributes = True


class SubtopicOut(BaseModel):
    id: int
    name: str
    topic_id: int

    class Config:
        from_attributes = True


class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    subtopic_id: int
    is_approved: bool

    class Config:
        from_attributes = True
