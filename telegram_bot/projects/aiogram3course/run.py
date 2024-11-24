import asyncio
import logging
from aiogram import Bot, Dispatcher


from config import BOT_TOKEN
from app.handlers import router

bot = Bot(token=BOT_TOKEN)  # сам бот, инициализация
dp = Dispatcher()  # диспетчер, основной роутер  - обрабатывает входящие обновления


async def main():
    # add router to dp 
    dp.include_router(router)
    #  отправляем запросы на телеграм сервер и если ответ есть, бот его обработает
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())