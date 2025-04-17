from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, DECIMAL
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from .orders import Order
    from .items import Item


class OrderItemAssociation(Base):
    __tablename__ = "order_item_association"
    __table_args__ = (
        UniqueConstraint("order_id", "item_id", name="idx_unique_order_product"),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("shop_app__orders.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("shop_app__items.id"))
    count: Mapped[int] = mapped_column(default=1, server_default="1")
    unit_price: Mapped[int] = mapped_column(DECIMAL(2), default=0, server_default="0")

    order: Mapped["Order"] = relationship(back_populates="items_details")
    item: Mapped["Item"] = relationship(back_populates="orders_details")
