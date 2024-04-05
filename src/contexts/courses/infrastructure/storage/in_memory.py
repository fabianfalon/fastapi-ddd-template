from typing import List, NoReturn, Optional

from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository


class InMemoryRepository(CourseRepository):
    def delete(self, course_id: str) -> NoReturn:
        print("mock delete")

    _courses: List[Course] = []

    def save(self, course: Course) -> NoReturn:
        self._courses.append(course)

    def find_one(self, course_id: str) -> Optional[Course]:
        return next(filter(lambda x: (x.id == course_id), self._courses), None)

    async def find_all(self) -> List[Course]:
        return self._courses

    def find_one_by_title(self, title) -> Optional[Course]:
        return next(filter(lambda x: (x.title == title), self._courses), None)

    def clear(self):
        self._courses = []
