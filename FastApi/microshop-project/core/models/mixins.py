from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, relationship
from sqlalchemy.orm import mapped_column

if TYPE_CHECKING:
    from .users import User


class UserRelationMixin:
    _user_id_nullable = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("shop_app__users.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    # back_populates same as related_name in Django
    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship("User", back_populates=cls._user_back_populates)
