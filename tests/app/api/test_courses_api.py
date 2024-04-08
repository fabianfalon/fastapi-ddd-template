from fastapi.testclient import TestClient

from src.main import app


class TestApi:
    client = TestClient(app)


class TestCoursesApi(TestApi):
    def test_create_new_course(self):
        data = {"title": "test-title", "duration": 10}
        response = self.client.post("/courses", json=data)
        assert response.status_code == 200

    def test_create_new_course_ko(self):
        data = {"title": "test-title", "duration": 10}
        response = self.client.post("/courses", json=data)
        assert response.status_code == 409

    def test_get_all_courses(self):
        response = self.client.get("/courses")
        assert response.status_code == 200
        assert response.json().get("courses") is not None

    def test_get_course_by_id_ko(self):
        response = self.client.get(f"/courses/12123123123111")
        assert response.status_code == 404
