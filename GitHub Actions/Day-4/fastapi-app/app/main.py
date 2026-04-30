from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.users import router as user_router
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title="🚀 Production FastAPI",
    description="Enterprise FastAPI with Docker, CI/CD, and AKS",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ✅ CORS (useful for UI / future frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include API routes
app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")


# ✅ Root UI (serves your index.html)
@app.get("/", response_class=HTMLResponse)
def home():
    with open("app/templates/index.html", "r") as f:
        return f.read()


# ✅ Health check (for Kubernetes / monitoring)
@app.get("/health")
def health():
    return {"status": "ok"}