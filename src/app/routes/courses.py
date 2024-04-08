from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as http_status

from src.app.controllers.courses.course_creator_controller import CourseCreateController
from src.app.controllers.courses.course_finder_controller import CourseFinderController
from src.app.controllers.courses.course_list_controller import ListCourseController
from src.app.routes.dependencies import (
    get_course_creator_controller,
    get_course_finder_controller,
    get_course_repository,
    get_list_course_controller,
)
from src.contexts.courses.domain.course_repository import CourseRepository
from src.contexts.courses.domain.errors.course_already_exists import CourseAlreadyExits
from src.contexts.courses.domain.errors.course_not_found import CourseNotFound
from src.contexts.courses.infrastructure.dto.course_dto import CourseIn, CourseListResponse, CourseOut
from src.contexts.shared.domain.value_objects.course_id import CourseId

# Router Config
router = APIRouter(tags=["Courses"])


@router.get(
    "/courses",
    summary="List all courses",
    status_code=http_status.HTTP_200_OK,
    response_model=CourseListResponse,
    response_model_exclude_none=True,
)
async def get_courses(
    controller: ListCourseController = Depends(get_list_course_controller),
    repository: CourseRepository = Depends(get_course_repository),
) -> CourseListResponse:
    courses = await controller.execute()
    courses = [CourseOut(**course.to_primitive()) for course in courses]
    return CourseListResponse(courses=courses)


@router.post(
    "/courses",
    summary="Create courses",
    status_code=http_status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def create_course(
    payload: CourseIn,
    controller: CourseCreateController = Depends(get_course_creator_controller),
    repository: CourseRepository = Depends(get_course_repository),
) -> CourseOut:
    title = payload.title
    duration = payload.duration
    try:
        course = await controller.execute(str(uuid4()), title, duration)
    except CourseAlreadyExits as exc:
        raise HTTPException(status_code=http_status.HTTP_409_CONFLICT, detail=exc.args[0]) from exc
    return CourseOut(**course.to_primitive())


@router.get(
    "/courses/{course_id}",
    summary="Get course by id",
    status_code=http_status.HTTP_200_OK,
    response_model_exclude_none=True,
)
async def get_course_by_id(
    course_id: str,
    controller: CourseFinderController = Depends(get_course_finder_controller),
    repository: CourseRepository = Depends(get_course_repository),
) -> CourseOut:
    try:
        course = await controller.execute(CourseId(course_id))
    except CourseNotFound as exc:
        raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail=exc.args[0]) from exc
    return CourseOut(**course.to_primitive())
