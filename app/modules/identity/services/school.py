from app.common.service.base import BaseService
from app.modules.identity.models.school import School
from app.modules.identity.repositories.school import SchoolRepository

from app.core.exceptions.business import ResourceNotFound


class SchoolService(BaseService[SchoolRepository, School]):

    model = School

    def __init__(self, repository: SchoolRepository):
        super().__init__(repository)

    def get(self, id):
        school = super().get(id)

        if school is None:
            raise ResourceNotFound("School not found")

        return school
