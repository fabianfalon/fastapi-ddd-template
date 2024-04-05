from uuid import uuid4

from src.app.controllers.controller import ControllerInterfaz
from src.contexts.courses.application.course_creator import CourseCreatorUseCase
from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository


class CourseCreateController(ControllerInterfaz):

    def __init__(self, repository: CourseRepository):
        self.repository = repository

    async def execute(self, course_id, title, duration) -> Course:
        course = await CourseCreatorUseCase(repository=self.repository).execute(
            str(uuid4()), title, duration
        )
        return course
