from typing import TYPE_CHECKING

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from .orders import Order
    from .order_item_association import OrderItemAssociation


class Item(Base):
    # MappedColumn - column in table
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[str] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text(255), nullable=True)

    orders: Mapped[list["Order"]] = relationship(
        secondary="order_item_association", back_populates="items"
    )

    orders_details: Mapped[list["OrderItemAssociation"]] = relationship(
        back_populates="item",
    )

    def __str__(self):
        return f"Item: id={self.id}, name={self.name!r}"

    def __repr__(self):
        return str(self)
