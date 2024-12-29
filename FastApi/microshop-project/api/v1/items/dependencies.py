from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.items import crud
from core.models import Item
from core.models import db_helper


async def get_item_by_id(
    item_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Item:
    item = await crud.get_item(session=session, item_id=item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found",
            headers=None,
        )
    return item
