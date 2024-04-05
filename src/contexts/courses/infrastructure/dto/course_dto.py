from datetime import datetime

from pydantic import BaseModel


class CourseOut(BaseModel):
    id: str
    title: str
    duration: float
    created_at: datetime
    updated_at: datetime


class CourseIn(BaseModel):
    title: str
    duration: float
