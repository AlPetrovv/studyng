__doc__ = """Directory for CRUD operations on users."""
from .schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()  # to dict
    return {
        "success": True,
        "user": user,
    }
