from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import agree_kb
from keyboards import tariffs_kb
from keyboards import pay_inkb
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет. Я бот. Чтобы продолжить работу, вы должны быть согласны со всеми правилами", 
                         reply_markup=agree_kb)


@router.message(lambda message: message.text and message.text.lower() == "согласиться")
async def answer_agree(message: Message):
    await message.answer(
        "Отлично. Теперь, нажмите на кнопку Тарифы, чтобы перейти к тарифам, или Назад, чтобы вернуться к команде Start.",
        reply_markup=tariffs_kb
    )
    
@router.message(lambda message: message.text and message.text.lower() == "тарифы")
async def answer_tariffs(message: Message):
    await message.answer("Чтобы оплатить, нажмите на кнопку ниже:", reply_markup=pay_inkb)


@router.message(lambda message: message.text and message.text.lower() == "не соглашаться")
async def answer_disagree(message: Message):
    await message.answer("К сожалению, без соглашения мы не можем предоставить вам доступ к материалу.", reply_markup=agree_kb)

@router.message(lambda message: message.text and message.text.lower() == "назад")
async def answer_disagree(message: Message):
    await message.answer("Вы вернулись к соглашению с правилами.", reply_markup=agree_kb)