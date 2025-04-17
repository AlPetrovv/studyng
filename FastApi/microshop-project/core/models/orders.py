from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


from .base import Base

if TYPE_CHECKING:
    from .items import Item
    from .order_item_association import OrderItemAssociation


class Order(Base):
    # MappedColumn - column in table
    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
    items: Mapped[list["Item"]] = relationship(
        secondary="order_item_association", back_populates="orders"
    )

    items_details: Mapped[list["OrderItemAssociation"]] = relationship(
        back_populates="order",
    )

    def __str__(self):
        return f"Order: id={self.id}"

    def __repr__(self):
        return str(self)
