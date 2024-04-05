from src.contexts.courses.domain.course_repository import CourseRepository


class CourseGetAllUseCase:
    def __init__(self, repository: CourseRepository) -> None:
        self.repository = repository

    def execute(self):
        courses = self.repository.find_all()
        return courses
