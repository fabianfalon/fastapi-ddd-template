from fastapi import Depends

from src.app.controllers.courses.course_creator_controller import CourseCreateController
from src.app.controllers.courses.course_finder_controller import CourseFinderController
from src.app.controllers.courses.course_list_controller import ListCourseController
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository


def get_course_repository() -> CourseRepository:
    return InMemoryRepository()


def get_course_creator_controller(
    repository: CourseRepository = Depends(get_course_repository),
) -> CourseCreateController:
    return CourseCreateController(repository=repository)


def get_course_finder_controller(
    repository: CourseRepository = Depends(get_course_repository),
) -> CourseFinderController:
    return CourseFinderController(repository=repository)


def get_list_course_controller(repository: CourseRepository = Depends(get_course_repository)) -> ListCourseController:
    return ListCourseController(repository=repository)
