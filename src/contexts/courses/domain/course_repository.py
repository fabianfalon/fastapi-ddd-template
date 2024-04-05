from abc import ABC, abstractmethod
from typing import List, NoReturn, Optional

from src.contexts.courses.domain.course import Course


class CourseRepository[T](ABC):
    """CourseRepository"""

    @abstractmethod
    def save(self, course: Course) -> Course: ...

    @abstractmethod
    def delete(self, course_id: str) -> NoReturn: ...

    @abstractmethod
    def find_one(self, course_id: str) -> Optional[Course]: ...

    @abstractmethod
    def find_all(self) -> List[Course]: ...

    @abstractmethod
    def find_one_by_title(self, title) -> Course: ...
