from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import UserRelationMixin

# hack circular import
# if now type checking (not run code)
if TYPE_CHECKING:
    # real import does not run
    # import only for check type checking
    from .users import User

# different between default and server_default
# default - use value when create obj by sqlalchemy
# server_default - default for database
# Mapped - not nullable if not use null like default


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"
    title: Mapped[str] = mapped_column(String(32), unique=True)
    body: Mapped[str] = mapped_column(
        Text,
        default="",  # default for alchemy
        server_default="",  # default for database
    )

    def __str__(self):
        return f"{self.__class__.__name__}: id={self.id}, user={self.user_id}"

    def __repr__(self):
        return str(self)
