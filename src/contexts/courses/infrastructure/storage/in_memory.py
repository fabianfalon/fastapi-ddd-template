from typing import List, Optional

from src.contexts.courses.domain.course import Course
from src.contexts.courses.domain.course_repository import CourseRepository


class InMemoryRepository(CourseRepository):
    def delete(self, course_id: str) -> None:
        print("mock delete")

    _courses: List[Course] = []

    async def save(self, course: Course) -> None:
        self._courses.append(course)

    async def find_one(self, course_id: str) -> Optional[Course]:
        return next(filter(lambda x: (x.id == course_id), self._courses), None)

    async def find_all(self) -> List[Course]:
        return self._courses

    async def find_one_by_title(self, title) -> Optional[Course]:
        return next(filter(lambda x: (x.title == title), self._courses), None)

    def clear(self):
        self._courses = []
