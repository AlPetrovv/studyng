import uuid
from typing import Any

from fastapi import Depends, HTTPException, Header, Response
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status

security = HTTPBasic()


def get_auth_user(
    credentials: HTTPBasicCredentials = Depends(security),
) -> HTTPBasicCredentials:
    if credentials.username.isalpha():
        return credentials
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username",
        headers={"WWW-Authenticate": "Basic"},
    )


static_token_by_user = {
    "123sdfsdf": "admin",
    "321sdfsdf": "user",
}


# Header - get data from headers directly
def get_auth_user_by_token(static_token: str = Header(alias="x-auth-token")):
    if username := static_token_by_user.get(static_token):
        return username
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )


COOKIES: dict[str, dict[str, Any]] = {}

COOKIE_SESSION_ID_KEY = "web-app-session-id"


def gen_session_id() -> str:
    return uuid.uuid4().hex


def get_session_by_user(
    auth_user: HTTPBasicCredentials = Depends(get_auth_user),
):
    response = Response()
    session_id = gen_session_id()
    COOKIES[session_id] = {
        "username": auth_user.username,
        "password": auth_user.password,
    }
    response.set_cookie(COOKIE_SESSION_ID_KEY, session_id)
    return response
