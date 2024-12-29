from fastapi.routing import APIRouter  # router for api

from . import crud  # for crud operations
from .schemas import CreateUser  # create user schema

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: CreateUser):
    """
    Create new user
    Annotation CreateUser shows to fastapi which params need to write to request body
    And Annotation CreateUser auto add validation for body params
    """
    return crud.create_user(user_in=user)
