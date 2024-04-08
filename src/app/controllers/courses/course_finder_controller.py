from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.course_finder import CourseFinderUseCase
from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound
from src.contexts.shared.domain.value_objects.course_id import CourseId


class CourseFinderController(ControllerInterfaz):
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    async def execute(self, course_id: CourseId) -> Course:
        try:
            course = CourseFinderUseCase(repository=self.repository).execute(course_id)
        except Exception as error:
            raise CourseNotFound(course_id.value) from error
        return course
