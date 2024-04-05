from datetime import datetime
from typing import List

from pydantic import BaseModel


class CourseOut(BaseModel):
    course_id: str
    title: str
    duration: float
    created_at: datetime
    updated_at: datetime


class CourseIn(BaseModel):
    title: str
    duration: float


class CourseListResponse(BaseModel):
    courses: List[CourseOut]
