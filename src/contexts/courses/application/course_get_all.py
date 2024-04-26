from typing import List

from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository


class CourseGetAllUseCase:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    async def execute(self) -> List[Course]:
        courses = await self.repository.find_all()
        return courses
