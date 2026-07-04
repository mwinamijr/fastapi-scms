from fastapi import Request, HTTPException
from app.modules.auth.service.token_service import decode_token
from app.core.tenant import set_tenant


def get_current_user(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        payload = decode_token(token)
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


def attach_tenant(user_payload: dict):
    set_tenant(user_payload["school_id"])
    return user_payload
