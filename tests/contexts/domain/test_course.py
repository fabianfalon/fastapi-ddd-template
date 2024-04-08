from uuid import uuid4

from src.contexts.courses.domain.course import Course


class TestCourseFactory:
    def test_create_new_course(self):
        course_id = str(uuid4())
        title = "title"
        duration = 1.0
        course = Course.create(course_id, title, duration)
        assert course.id == course_id
        assert course.title == title
        assert course.duration == duration

    def test_create_from_primitive(self):
        course_id = str(uuid4())
        title = "title2"
        duration = 1.0
        course = Course.from_primitive({"_id": course_id, "title": title, "duration": duration})
        assert course.id == course_id
        assert course.title == title
        assert course.duration == duration

    def test_convert_course_to_primitive(self):
        course_id = str(uuid4())
        title = "title2"
        duration = 1.0
        course = Course.create(course_id, title, duration)
        assert course.to_primitive().get("course_id") == course_id
        assert course.to_primitive().get("title") == title
        assert course.to_primitive().get("duration") == duration
