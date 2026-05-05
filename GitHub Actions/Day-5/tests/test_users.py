from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_auth_headers():
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "admin123"}
    )
    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def test_create_user():
    headers = get_auth_headers()

    response = client.post(
        "/api/v1/users/",
        json={"name": "Test", "email": "test@example.com"},
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test"


def test_get_users():
    headers = get_auth_headers()

    response = client.get(
        "/api/v1/users/",
        headers=headers
    )

    assert response.status_code == 200
