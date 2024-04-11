from uuid import uuid4

import pytest
from expects import be_above_or_equal, equal, expect, raise_error

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
        duration = 10
        use_case = CourseCreatorUseCase(get_course_repository())
        course = await use_case.execute(course_id, title, duration)
        expect(course.id).to(equal(course_id))
        expect(course.title).to(equal(title))
        expect(course.duration).to(equal(duration))

    async def test_create_new_course_ko(self):
        course_id = str(uuid4())
        title = "title"
        duration = 1.0
        use_case = CourseCreatorUseCase(get_course_repository())

        with pytest.raises(CourseAlreadyExits) as error:
            await use_case.execute(course_id, title, duration)
        expect(error.value.args[0]).to(equal("Course with this title already exits."))

    async def test_get_course_by_course_id(self):
        course_id = str(uuid4())
        title = f"title {course_id}"
        duration = 20
        use_case = CourseCreatorUseCase(get_course_repository())
        await use_case.execute(course_id, title, duration)

        use_case = CourseFinderUseCase(get_course_repository())
        course = await use_case.execute(CourseId(course_id))
        expect(course.id).to(equal(course_id))
        expect(course.title).to(equal(title))
        expect(course.duration).to(equal(duration))

    async def test_get_all_courses(self):
        course_id = str(uuid4())
        title = f"title {course_id}"
        duration = 1.0
        repository = get_course_repository()
        use_case = CourseCreatorUseCase(repository)
        await use_case.execute(course_id, title, duration)

        use_case = CourseGetAllUseCase(repository)
        courses = await use_case.execute()
        expect(len(courses)).to(be_above_or_equal(1))
