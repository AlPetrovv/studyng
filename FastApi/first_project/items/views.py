from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Path

"""
Что такое router - по факту это простарнство имен для путей.
prefix - пространство имен для путей
tags - тэги для swagger (блоки для документации)
"""
router = APIRouter(prefix='/items', tags=['Items'])

@router.get('/')
def list_items():
    return {'items': ['item1', 'item2', 'item4', ]}


@router.get('/latest/')
def get_latest_item():
    return {'item_id': 3}


@router.get('/{item_id}')
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    """
    Annotated[int, Path(ge=1, lt=1_000_000)] - что это такое?
    Annotated - служит для обозначения и комбинации правил в анотации
    1 аргумент - это тип к которому будут применены правила
    2 аргумент - правила для этого типа
    В данном случае Path указывает, что мы задаем правила для пути, а ge=1, lt=1_000_000 - правила
    """
    return {
        'item_id': {
            'id': item_id
        },
    }
