"""Course Domain"""

from datetime import datetime

import pytz

from src.config import settings
from src.contexts.courses.domain.value_objects.course_duration import CourseDuration
from src.contexts.courses.domain.value_objects.course_title import CourseTitle
from src.contexts.shared.aggregate_root import AggregateRoot
from src.contexts.shared.domain.value_objects.course_id import CourseId


class Course(AggregateRoot):
    _id: CourseId
    _title: CourseTitle
    _duration: CourseDuration
    updated_at: datetime
    created_at: datetime

    def __init__(
        self,
        course_id: str,
        title: str,
        duration: float,
        created_at: datetime = None,
        updated_at: datetime = None,
    ) -> None:
        self._id = CourseId(course_id)
        self._title = CourseTitle(title)
        self._duration = CourseDuration(duration)
        self.created_at = created_at if created_at else datetime.now(tz=pytz.timezone(settings.timezone))
        self.updated_at = updated_at if updated_at else datetime.now(tz=pytz.timezone(settings.timezone))

    @property
    def id(self):
        return self._id.value

    @property
    def title(self):
        return self._title.value

    @property
    def duration(self):
        return self._duration.value

    @staticmethod
    def create(course_id, title, duration):
        """Creates a new Course."""
        tz = pytz.timezone(settings.timezone)
        course = Course(
            course_id=course_id,
            title=title,
            duration=duration,
            updated_at=datetime.now(tz=tz),
            created_at=datetime.now(tz=tz),
        )

        # logic to public domain event
        return course

    @staticmethod
    def from_primitive(raw_data: dict) -> AggregateRoot:
        return Course(
            course_id=raw_data.get("_id"),
            title=raw_data.get("title"),
            duration=raw_data.get("duration"),
            created_at=raw_data.get("created_at"),
            updated_at=raw_data.get("updated_at"),
        )

    def to_primitive(self):
        return {
            "course_id": self.id,
            "title": self.title,
            "duration": self.duration,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
