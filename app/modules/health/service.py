from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from .schema import HealthResponse


class HealthService:
    def __init__(self, repo):
        self.repo = repo

    def system_status(self):
        try:
            version = self.repo.database_version()
            server_time = self.repo.database_time()

            return HealthResponse(
                status="UP",
                service=settings.PROJECT_NAME,
                version=settings.VERSION,
                environment=settings.ENVIRONMENT,
                database=version,
                server_time=server_time,
            )
        except SQLAlchemyError:
            return {
                "status": "DOWN",
                "servive": settings.PROJECT_NAME,
                "version": settings.VERSION,
                "environment": settings.ENVIRONMENT,
                "database": "Unavailable",
                "server_time": None,
            }
