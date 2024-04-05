from src.contexts.courses.infrastructure.storage.in_memory import InMemoryRepository
from src.contexts.courses.domain.course_repository import CourseRepository


def get_course_repository() -> CourseRepository:
    return InMemoryRepository()
