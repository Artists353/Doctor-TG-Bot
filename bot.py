import asyncio
from aiogram import Bot, Dispatcher, types
from api_token import TOKEN
from handlers import agree_handler


async def main():
    bot = Bot(TOKEN) 
    dp = Dispatcher()
    dp.include_router(agree_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())