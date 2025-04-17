from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .users import User


class UserRelationMixin:
    """Mixin that autogenerate relation for User model"""

    _user_id_nullable = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        """Declared attribute user_id for relation with User model"""
        return mapped_column(
            ForeignKey("shop_app__users.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    # back_populates same as related_name in Django
    @declared_attr
    def user(cls) -> Mapped["User"]:
        """Create relationship to User model"""
        return relationship("User", back_populates=cls._user_back_populates)
