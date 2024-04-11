from src.contexts.courses.domain.course_repository import CourseRepository


class CourseGetAllUseCase:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    async def execute(self):
        courses = await self.repository.find_all()
        return courses
