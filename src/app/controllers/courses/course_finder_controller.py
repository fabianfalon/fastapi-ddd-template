from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.course_finder import CourseFinderUseCase
from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound


class CourseFinderController(ControllerInterfaz):

    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    async def execute(self, course_id) -> Course:
        try:
            course = await CourseFinderUseCase(repository=self.repository).execute(course_id)
        except Exception as error:
            raise CourseNotFound(course_id) from error
        return course
