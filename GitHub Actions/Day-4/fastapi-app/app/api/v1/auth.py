from fastapi import APIRouter, HTTPException
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

# fake user (demo only)
fake_user = {
    "username": "admin",
    "password": "admin123"
}


@router.post("/login")
def login(data: dict):
    if data.get("username") != fake_user["username"] or data.get("password") != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": data["username"]})

    return {
        "access_token": token,
        "token_type": "bearer"
    }