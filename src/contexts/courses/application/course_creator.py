from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.value_objects.course_title import CourseTitle


class CourseCreatorUseCase:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    async def execute(self, course_id: str, title: str, duration: float):
        recorded = await self.repository.find_one_by_title(CourseTitle(title).value.lower().strip())
        if recorded:
            raise CourseAlreadyExits()

        course = Course.create(course_id, title, duration)
        await self.repository.save(course)
        return course
