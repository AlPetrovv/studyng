from aiogram import BaseMiddleware
from typing import Callable, Any, Dict, Awaitable
from aiogram.types import TelegramObject


# Create middleware (you can use as inner and outer middleware)
# If you use the middleware as inner middleware it works inner router view (filter)
# If you use the middleware as outer middleware it works before view is working
# Summary: if you send message that don't fit any pattern
# will be work outer middleware and inner middleware didn't work
class TestMiddleware(BaseMiddleware):
    # __call__ -> ...
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        print('Do smth before handler')
        # result ->
        result = await handler(event, data)
        print('Do smth after handler')
        return result
