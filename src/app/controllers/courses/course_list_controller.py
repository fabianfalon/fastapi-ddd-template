from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.course_get_all import CourseGetAllUseCase
from src.contexts.courses.domain.course import Course


class ListCourseController(ControllerInterfaz):
    def __init__(self, repository):
        self.repository = repository

    async def execute(self) -> Course:
        course = await CourseGetAllUseCase(repository=self.repository).execute()
        return course
