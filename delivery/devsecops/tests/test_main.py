from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Secure DevSecOps App" in response.text

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# --- DevSecOps Security Regression Test ---
def test_security_headers():
    """
    YouTube Tip: Explain that we test for security headers to 
    prevent Clickjacking and Sniffing attacks.
    """
    response = client.get("/")
    # Check for security headers that a production FastAPI app should have
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert "X-Frame-Options" in response.headers