import asyncio
from aiogram import Bot, Dispatcher, types, F 
from aiogram.filters.command import Command, CommandObject 
from api_token import TOKEN
from aiogram.enums import ParseMode 
from aiogram.types import FSInputFile, KeyboardButton, ReplyKeyboardMarkup 


bot = Bot('7560534293:AAHPWzyz5Zdm4_uprE2SIjPV4TZoyIwjJzI') 
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Приветствие и объяснение')
    

async def main():
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == '__main__':
    asyncio.run(main())