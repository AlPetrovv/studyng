from fastapi import APIRouter
from fastapi import Depends  # dependency for FastAPI
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Item
from core.models import db_helper

from . import crud
from . import schemas
from .dependencies import get_item_by_id

router = APIRouter(prefix="/items", tags=["Items"])


# Depends - in this time provides dependency for handlers
# it means that this dependency will be used in handlers
# How it works?
# 1. FastAPI call func dp_helper.session_dependency
# 2. FastAPI provide session from func to handler
# 3. FastAPI after handler close session (after yield)


# response_model - response as model from pydantic schema
# response -> {ItemGet, ItemGet, ItemGet}
@router.get("/", response_model=list[schemas.ItemGet])
async def get_items(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_items(session=session)


@router.post("/", response_model=schemas.ItemCreate)
async def create_item(
    item_in: schemas.ItemCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_item(session=session, item_in=item_in)


@router.get("/{item_id}/", response_model=schemas.ItemGet)
async def get_item(item: Item = Depends(get_item_by_id)):
    return item


@router.put("/{item_id}/", response_model=schemas.ItemUpdate)
async def update_item(
    item_in: schemas.ItemUpdate,
    item: Item = Depends(get_item_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_item(session=session, item_in=item_in, item=item)


@router.patch("/{item_id}/", response_model=schemas.ItemUpdatePartial)
async def update_partial_item(
    item_in: schemas.ItemUpdatePartial,
    item: Item = Depends(get_item_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_item(
        session=session, item_in=item_in, item=item, partial=True
    )


@router.delete("/{item_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item: Item = Depends(get_item_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_item(session, item)
