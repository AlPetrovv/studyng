from typing import List

from sqlalchemy import select  # util for create query to db
from sqlalchemy.engine import Result  # return from execute command
from sqlalchemy.ext.asyncio import AsyncSession  # for work with db

from core.models import Item

from . import schemas


async def get_items(session: AsyncSession) -> List[Item]:
    # select Items from db by id order (this is only command to db)
    stmt = select(Item).order_by(Item.id)
    # execute command from bellow string
    result: Result = await session.execute(stmt)
    # scalars - generator
    items = result
    # all -> return Sequence
    items = items.scalars().all()
    return list(items)


# get by id
async def get_item(session: AsyncSession, item_id: int) -> Item | None:
    # session.get - return one item
    # first elem - entity(Model that has id), second elem is identification param
    return await session.get(Item, item_id)


# post item
async def create_item(session: AsyncSession, item_in: schemas.ItemCreate) -> Item:
    # create new item
    item = Item(**item_in.model_dump())
    # add to session (session follow item)
    session.add(item)
    # commit changes save to db
    await session.commit()
    # await session.refresh(item) # refresh item
    return item


async def update_item(
    session: AsyncSession,
    item_in: schemas.ItemUpdate | schemas.ItemUpdatePartial,
    item: Item,
    partial: bool = False,
) -> Item:
    for attr, value in item_in.model_dump(
        exclude_unset=partial,
        exclude_defaults=partial,
    ).items():
        setattr(item, attr, value)
    await session.commit()

    return item


async def delete_item(session: AsyncSession, item: Item) -> None:
    await session.delete(item)
    await session.commit()
