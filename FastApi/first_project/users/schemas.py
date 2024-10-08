__doc__ = """Schemas of serialization data for users."""

from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MaxLen, MinLen


class CreateUser(BaseModel):
    """
    В общем что тут такое происходит:
    BaseModel - что-то похожее на dataclass, но с поддержкой аннотаций + валидацией
    email: EmailStr - встроенная валидация по email от FastApi

    username: str = Field(..., max_digits=3, max_length=20)
    ВАЖНО: ... - показывают что поле обязательное!
    Field - пока не понятно, но используется для pydantic моделей, в нем есть встроенная валидация

    username: Annotated[str,MinLen(3),MaxLen(20),] другой метод валидации полей
    """

    email: EmailStr
    # username: str = Field(..., max_digits=3, max_length=20)
    username: Annotated[
        str,
        MinLen(3),
        MaxLen(20),
    ]
