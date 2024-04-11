from abc import ABC, abstractmethod
from typing import List, NoReturn, Optional

from src.contexts.courses.domain.course import Course


class CourseRepository[T](ABC):
    """CourseRepository"""

    @abstractmethod
    async def save(self, course: Course) -> Course: ...

    @abstractmethod
    async def delete(self, course_id: str) -> NoReturn: ...

    @abstractmethod
    async def find_one(self, course_id: str) -> Optional[Course]: ...

    @abstractmethod
    async def find_all(self) -> List[Course]: ...

    @abstractmethod
    async def find_one_by_title(self, title) -> Course: ...
