from expects import be, be_none, expect
from fastapi.testclient import TestClient
from starlette import status

from src.main import app


class TestApi:
    client = TestClient(app)


class TestCoursesApi(TestApi):
    def test_create_new_course(self):
        data = {"title": "test-title", "duration": 10}
        response = self.client.post("/courses", json=data)
        expect(response.status_code).to(be(status.HTTP_200_OK))

    def test_create_new_course_ko(self):
        data = {"title": "test-title", "duration": 10}
        response = self.client.post("/courses", json=data)
        expect(response.status_code).to(be(status.HTTP_409_CONFLICT))

    def test_get_all_courses(self):
        response = self.client.get("/courses")
        expect(response.status_code).to(be(status.HTTP_200_OK))
        expect(response.json().get("courses")).not_to(be_none)

    def test_get_course_by_id_ko(self):
        response = self.client.get(f"/courses/12123123123111")
        expect(response.status_code).to(be(status.HTTP_404_NOT_FOUND))
