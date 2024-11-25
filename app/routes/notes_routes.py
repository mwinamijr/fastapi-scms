import os
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models.user_models import UserRole
from app.models.notes_models import Illustration
from app.schemas.notes_schemas import *
from app.crud import notes_crud


# Directory to store uploaded images
UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

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


@router.post("/illustrations", response_model=IllustrationResponse)
async def add_illustration(
    content: str,
    note_id: int,
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
):
    """
    Create a new illustration with optional image upload.
    """
    image_path = None

    if file:
        # Save uploaded file
        file_extension = os.path.splitext(file.filename)[1]
        if file_extension.lower() not in [".png", ".jpg", ".jpeg", ".gif"]:
            raise HTTPException(
                status_code=400, detail="Invalid file type. Only images are allowed."
            )
        image_path = f"{UPLOAD_DIR}/{file.filename}"
        with open(image_path, "wb") as f:
            f.write(await file.read())

    illustration_data = {"content": content, "note_id": note_id, "image": image_path}
    return notes_crud.create_illustration(db, illustration_data)


@router.patch("/illustrations/{illustration_id}", response_model=IllustrationResponse)
def modify_illustration(
    illustration_id: int,
    description: Optional[str] = None,
    image: Optional[str] = None,
    db: Session = Depends(get_db),
):
    updated_illustration = notes_crud.update_illustration(
        db, illustration_id, description, image
    )
    if not updated_illustration:
        raise HTTPException(status_code=404, detail="Illustration not found")
    return updated_illustration
