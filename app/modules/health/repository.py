from sqlalchemy import text
from sqlalchemy.orm import Session


class HealthRepository:
    def __init__(self, db: Session):
        self.db = db

    def database_alive(self):
        self.db.execute(text("SELECT 1"))

        return True

    def database_version(self):
        return self.db.execute(text("SELECT version()")).scalar()

    def database_time(self):
        return self.db.execute(text("SELECT NOW()")).scalar()
