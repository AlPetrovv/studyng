from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .posts import Post


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped[Profile] = relationship(back_populates="user")
