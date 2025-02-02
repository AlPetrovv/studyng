from sqlalchemy import DECIMAL, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .base import Base


class Order(Base):
    # MappedColumn - column in table
    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
