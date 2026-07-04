from app.common.service.base import BaseService
from app.modules.identity.models.school import School
from app.modules.identity.repositories.school import SchoolRepository


class SchoolService(BaseService[SchoolRepository, School]):

    model = School

    def __init__(self, repository: SchoolRepository):
        super().__init__(repository)
