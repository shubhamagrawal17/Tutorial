from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
import pickle

app = FastAPI(
    title="DevSecOps Demo App",
    description="Secure CI/CD with Azure DevOps, Bandit, pip-audit",
    version="1.0.0",
)

# -------------------------
# Production-Grade Security Middleware
# -------------------------
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """
    Injects security headers into every response.
    This fulfills the security regression tests in our pipeline.
    """
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

# -------------------------
# Home Page (HTML)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>DevSecOps App</title>
        </head>
        <body style="font-family: Arial; background-color: #f4f6f8; padding: 40px;">
            <h1>🚀 Secure DevSecOps App</h1>
            <p>This application is protected by <b>High-Confidence Security Gates</b>.</p>
            <hr>
            <ul>
                <li><a href="/about">About the Stack</a></li>
                <li><a href="/status">Pipeline Security Status</a></li>
                <li><a href="/health">Health Check (JSON)</a></li>
                <li><a href="/docs">API Docs (Swagger)</a></li>
            </ul>
        </body>
    </html>
    """

# -------------------------
# Health Check & Status
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/status")
def status():
    return {
        "security_layers": {
            "SAST": "Bandit (Custom SARIF Reporting)",
            "SCA": "pip-audit (High/Critical/Unknown Gate)",
            "Testing": "Pytest with 80% Coverage Gate"
        },
        "infrastructure": "AKS / Azure DevOps"
    }

# -------------------------
# ⚠️ SAST Demo: Vulnerable Endpoint
# This is designed to trigger Bandit B301 (Pickle Deserialization)
# -------------------------
@app.post("/process-data", include_in_schema=False)
def process_data(data: bytes):
    # This will be flagged as HIGH severity / HIGH confidence by Bandit
    return pickle.loads(data)

# -------------------------
# About Page
# -------------------------
@app.get("/about")
def about():
    return {
        "app": "DevSecOps Demo",
        "stack": ["FastAPI", "Docker", "AKS", "Azure DevOps"],
        "security": ["SAST", "Dependency Scan", "Container Scan"],
    }