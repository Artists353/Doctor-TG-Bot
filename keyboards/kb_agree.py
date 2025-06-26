from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def agree_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = 'Согласен')
    kb.button(text = 'Не согласен')
    return kb.as_markup(resize_keyboard = True)