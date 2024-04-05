from src.app.controllers.courses.course_creator_controller import CourseCreateController
from src.app.controllers.courses.course_finder_controller import CourseFinderController
from src.app.controllers.courses.course_list_controller import ListCourseController
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository


def get_course_repository() -> CourseRepository:
    return InMemoryRepository()


def get_course_creator_controller() -> CourseCreateController:
    repository = get_course_repository()
    return CourseCreateController(repository=repository)


def get_course_finder_controller() -> CourseFinderController:
    repository = get_course_repository()
    return CourseFinderController(repository=repository)


def get_list_course_controller() -> ListCourseController:
    repository = get_course_repository()
    return ListCourseController(repository=repository)
