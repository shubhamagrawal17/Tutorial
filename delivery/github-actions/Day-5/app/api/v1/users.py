from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


# ✅ Create User (Protected)
@router.post("/", response_model=UserResponse)
def create_user(
    payload: UserCreate,
    user: str = Depends(get_current_user)
):
    return UserService.create_user(payload.name, payload.email)


# ✅ Get All Users (Protected)
@router.get("/", response_model=List[UserResponse])
def list_users(
    user: str = Depends(get_current_user)
):
    return UserService.get_users()


# ✅ Get User by ID (Protected)
@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    user: str = Depends(get_current_user)
):
    user_data = UserService.get_user(user_id)

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    return user_data


# ✅ Delete User (Protected)
@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    user: str = Depends(get_current_user)
):
    success = UserService.delete_user(user_id)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "message": "User deleted successfully",
        "deleted_user_id": user_id
    }