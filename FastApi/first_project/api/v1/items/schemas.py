__doc__ = """Schemas of serialization data for users. Smth like serializers in Django"""

from pydantic import BaseModel
from pydantic import ConfigDict  # pydantic {config} package


# Base Item schema for crud operations, ok
# id not declared because if use it in get and post - user can change and see id
# because we use different schemas for get and post
class ItemBase(BaseModel):
    name: str
    description: str
    price: int


# for create
class ItemCreate(ItemBase):
    pass


# for get
class ItemGet(ItemBase):
    # get name, description, price, id from attributes
    model_config = ConfigDict(from_attributes=True)
    id: int


class ItemUpdate(ItemBase):
    id: int


class ItemUpdatePartial(ItemBase):
    # option params
    # if defined None or another value - param not required
    name: str | None = None
    description: str | None = None
    price: int | None = None
