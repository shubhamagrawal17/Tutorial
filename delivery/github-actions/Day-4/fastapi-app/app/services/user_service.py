from typing import List, Optional
from app.models.user import User
from app.db.fake_db import DB


class UserService:

    # ✅ Create User
    @staticmethod
    def create_user(name: str, email: str) -> User:
        user = User(id=len(DB) + 1, name=name, email=email)
        DB.append(user)
        return user

    # ✅ Get All Users
    @staticmethod
    def get_users() -> List[User]:
        return DB

    # ✅ Get User by ID
    @staticmethod
    def get_user(user_id: int) -> Optional[User]:
        for user in DB:
            if user.id == user_id:
                return user
        return None

    # ✅ Delete User
    @staticmethod
    def delete_user(user_id: int) -> bool:
        for index, user in enumerate(DB):
            if user.id == user_id:
                DB.pop(index)
                return True
        return False