from uuid import uuid4

import pytest

from src.app.routes.dependencies import get_course_repository
from src.contexts.courses.application.course_creator import CourseCreatorUseCase
from src.contexts.courses.application.course_finder import CourseFinderUseCase
from src.contexts.courses.application.course_get_all import CourseGetAllUseCase
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.shared.domain.value_objects.course_id import CourseId


class TestCourseUseCases:
    async def test_create_new_course(self):
        course_id = str(uuid4())
        title = "title"
        duration = 1.0
        use_case = CourseCreatorUseCase(get_course_repository())
        course = await use_case.execute(course_id, title, duration)
        assert course.id == course_id
        assert course.title == title
        assert course.duration == duration

    async def test_create_new_course_ko(self):
        course_id = str(uuid4())
        title = "title"
        duration = 1.0
        use_case = CourseCreatorUseCase(get_course_repository())

        with pytest.raises(CourseAlreadyExits) as error:
            await use_case.execute(course_id, title, duration)
        assert error.value.args[0] == "Course with this title already exits."

    async def test_get_course_by_course_id(self):
        course_id = str(uuid4())
        title = f"title {course_id}"
        duration = 1.0
        use_case = CourseCreatorUseCase(get_course_repository())
        await use_case.execute(course_id, title, duration)

        use_case = CourseFinderUseCase(get_course_repository())
        course = use_case.execute(CourseId(course_id))
        assert course.id == course_id
        assert course.title == title
        assert course.duration == duration

    async def test_get_all_courses(self):
        course_id = str(uuid4())
        title = f"title {course_id}"
        duration = 1.0
        use_case = CourseCreatorUseCase(get_course_repository())
        await use_case.execute(course_id, title, duration)

        use_case = CourseGetAllUseCase(get_course_repository())
        courses = await use_case.execute()
        assert len(courses) >= 1
