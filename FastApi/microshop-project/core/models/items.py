from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import MappedColumn

from .base import Base


class Item(Base):
    # MappedColumn - column in table
    name = MappedColumn(String(255), nullable=False)
    price = MappedColumn(Integer, nullable=False)
    description = MappedColumn(Text(255), nullable=True)
