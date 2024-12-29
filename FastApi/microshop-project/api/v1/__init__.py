from fastapi import APIRouter

from core.config import settings

from .items.handlers import router as api_items_router

__all__ = ("router",)
router = APIRouter()

router.include_router(api_items_router, prefix=settings.api_v1_prefix)
