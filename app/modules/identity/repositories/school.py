from app.common.repository.base import BaseRepository
from app.modules.identity.models.school import School


class SchoolRepository(BaseRepository[School]):

    def __init__(self, db):
        super().__init__(School, db)

    def get_school_by_code(self, code: str):
        return self.db.query(School).filter(School.code == code).first()
