import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command, CommandObject 
from api_token import TOKEN
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile, KeyboardButton, ReplyKeyboardMarkup 
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
bot = Bot('7560534293:AAHPWzyz5Zdm4_uprE2SIjPV4TZoyIwjJzI') 
dp = Dispatcher()



@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Привет. Я бот. Чтобы продолжить работу, вы должны быть согласны со всеми правилами?')
    kb_agree = [
        [KeyboardButton(text = 'Согласиться.')],
        [KeyboardButton(text = 'Не соглашаться.')]
    ]
    keyboard_start = ReplyKeyboardMarkup(keyboard=kb_agree, one_time_keyboard=True, resize_keyboard=True, is_persistent=True)
    await message.answer('Вы согласны?', reply_markup=keyboard_start)


@dp.message(F.text.lower() == 'согласиться.')
async def agree(message: types.Message):
    await message.reply('Отлично. Теперь, нажмите на кнопку "Тарифы", чтобы перейти к тарифам, или "Назад", чтобы вернуться к команде "Start".')
    kb_tariff = [
        [KeyboardButton(text = 'Тарифы')],
        [KeyboardButton(text = 'Назад')]
    ]
    keyboard_tariffs = ReplyKeyboardMarkup(keyboard=kb_tariff, one_time_keyboard=True, resize_keyboard=True, is_persistent=True)
    await message.reply('Выберете', reply_markup=keyboard_tariffs)  


@dp.message(F.text.lower() == 'не cоглашаться.')
async def agree(message: types.Message):
    await message.reply('К сожалению, без соглашения мы не можем предоставить вам доступ к материалу.')

@dp.message(F.text.lower == 'тарифы.') 
async def tariffs(message: types.message):
    builder = InlineKeyboardBuilder()
    builder.row(text = 'Оплата в Юкасса', url='https://yookassa.ru/')
    await message.answer('Чтобы получить тарифы, нужно произвести оплату в размере ____ по ссылке ниже.', reply_markup = builder) 
   
    

async def main():
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == '__main__':
    asyncio.run(main())