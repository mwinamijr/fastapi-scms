from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.modules.auth.schema.auth import LoginSchema
from app.modules.auth.service.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(payload: LoginSchema, response: Response, db: Session = Depends(get_db)):
    service = AuthService(db)

    user = service.authenticate_user(payload.phone, payload.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    tokens = service.generate_tokens(user)

    response.set_cookie(
        key="access_token", value=tokens["access_token"], httponly=True, samesite="lax"
    )

    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        samesite="lax",
    )

    return {"message": "Login sucessful"}
