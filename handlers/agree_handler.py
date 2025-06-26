from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.kb_agree import kb_agree

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет. Я бот. Чтобы продолжить работу, вы должны быть согласны со всеми правилами?", 
                         reply_markup=kb_agree())


@router.message(lambda message: message.text and message.text.lower() == "согласиться")
async def answer_agree(message: Message):
    await message.answer(
        "Отлично. Теперь, нажмите на кнопку Тарифы, чтобы перейти к тарифам, или Назад, чтобы вернуться к команде Start.",
        reply_markup=ReplyKeyboardRemove()
    )
@router.message(lambda message: message.text and message.text.lower() == "не соглашаться")
async def answer_disagree(message: Message):
    await message.answer(
        "К сожалению, без соглашения мы не можем предоставить вам доступ к материалу.",
        reply_markup=ReplyKeyboardRemove()
    )