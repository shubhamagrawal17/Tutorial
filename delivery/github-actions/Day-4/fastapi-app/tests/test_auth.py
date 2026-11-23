from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():
    response = client.post("/api/v1/auth/login", json={
        "username": "admin",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_failure():
    response = client.post("/api/v1/auth/login", json={
        "username": "wrong",
        "password": "wrong"
    })
    assert response.status_code == 401
