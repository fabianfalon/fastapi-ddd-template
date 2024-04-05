from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends
from fastapi import status as http_status

from src.app.routes.dependencies import get_course_repository
from src.contexts.courses.application.course_creator import CourseCreatorUseCase
from src.contexts.courses.application.course_finder import CourseFinderUseCase
from src.contexts.courses.application.course_get_all import CourseGetAllUseCase
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound
from src.contexts.courses.infrastructure.dto.course_dto import CourseOut, CourseIn
from src.contexts.shared.domain.value_objects.course_id import CourseId

# Router Config
router = APIRouter(tags=["Courses"])


@router.get(
    "/courses",
    summary="List all courses",
    status_code=http_status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def get_courses(
    repository: CourseRepository = Depends(get_course_repository),
) -> List[CourseOut]:
    courses = await CourseGetAllUseCase(repository=repository).execute()
    if not courses:
        return []
    return courses


@router.post(
    "/courses",
    summary="Create courses",
    status_code=http_status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def create_course(
    payload: CourseIn,
    repository: CourseRepository = Depends(get_course_repository),
) -> CourseOut:
    title = payload.title
    duration = payload.duration
    course = await CourseCreatorUseCase(repository=repository).execute(str(uuid4()), title, duration)
    return course


@router.get(
    "/courses/{course_id}",
    summary="Get course by id",
    status_code=http_status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def get_course_by_id(
    course_id: str,
    repository: CourseRepository = Depends(get_course_repository),
) -> CourseOut:
    try:
        course = await CourseFinderUseCase(repository=repository).execute(CourseId(course_id))
    except CourseNotFound as exc:
        raise CourseNotFound(course_id) from exc
    course = course.to_primitive()
    return CourseOut(id=course.get("course_id"), **course)
