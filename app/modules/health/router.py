from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from .repository import HealthRepository
from .service import HealthService
from .schema import HealthResponse

router = APIRouter()


def get_health_service(
    db: Session = Depends(get_db),
):
    repo = HealthRepository(db)
    return HealthService(repo)


@router.get(
    "/",
    response_model=HealthResponse,
)
def health(service=Depends(get_health_service)):
    return service.system_status()
