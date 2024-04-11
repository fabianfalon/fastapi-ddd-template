from uuid import uuid4

from expects import expect, equal, have_key, have_keys

from src.contexts.courses.domain.course import Course


class TestCourseFactory:
    def test_create_new_course(self):
        course_id = str(uuid4())
        title = "title"
        duration = 1.0
        course = Course.create(course_id, title, duration)
        expect(course.id).to(equal(course_id))
        expect(course.title).to(equal(title))
        expect(course.duration).to(equal(duration))

    def test_create_from_primitive(self):
        course_id = str(uuid4())
        title = "title2"
        duration = 1.0
        course = Course.from_primitive({"_id": course_id, "title": title, "duration": duration})
        expect(course.id).to(equal(course_id))
        expect(course.title).to(equal(title))
        expect(course.duration).to(equal(duration))

    def test_convert_course_to_primitive(self):
        course_id = str(uuid4())
        title = "title2"
        duration = 1.0
        course = Course.create(course_id, title, duration)
        expect(course.to_primitive()).to(have_keys("title", "duration", "course_id"))
        expect(course.to_primitive()).to(have_key("title", "title2"))
