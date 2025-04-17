from typing import Annotated

from fastapi import APIRouter, Cookie, HTTPException, Response
from fastapi.params import Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status

from api.v1.demo_auth.dependencies import (
    get_auth_user,
    get_auth_user_by_token,
    get_session_by_user,
    COOKIE_SESSION_ID_KEY,
    COOKIES,
)

router = APIRouter(prefix="/demo_auth", tags=["Demo Auth"])

#
security = HTTPBasic()


# Annotated - служит для обозначения и комбинации правил в анотации
# 1 аргумент - это тип к которому будут применены правила
# 2 аргумент - это правила
# In this case we use HTTPBasicCredentials as Pydantic model and HTTPBasic as dependency for get credentials from headers
# steps:
# 1. FastAPI watch that has dependency HTTPBasic
# 2 FastAPI provide request to dependency
# 3. HTTPBasic return HTTPBasicCredentials from request with username and password
# 4. FastAPI provide data to handler (password and username)
@router.get("/basic_auth/")
def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {
        "message": "Hi!",
        "username": credentials.username,
        "password": credentials.password,
    }


@router.get("/basic_auth_new/")
def demo_basic_auth_credentials(
    auth_user: HTTPBasicCredentials = Depends(get_auth_user),
):
    return {
        "message": "Hi!",
        "user": auth_user,
    }


@router.get("/token_auth/")
def demo_basic_token_auth_credentials(
    auth_user_username: str = Depends(get_auth_user_by_token),
):
    return {
        "message": "Hi!",
        "username": auth_user_username,
    }


def get_session_data(
    session_id: str = Cookie(alias=COOKIE_SESSION_ID_KEY),
):
    if session_id not in COOKIES:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return COOKIES[session_id]


@router.post("/cookie_auth/")
def demo_cookie_auth(
    response=Depends(get_session_by_user),
):
    return response


@router.get("/check_cookie/")
def demo_auth_check_cookie(session_data: dict = Depends(get_session_data)):
    return session_data
