from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def kb_agree() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = "Соглaситься")
    kb.button(text = "Не соглашаться")
    return kb.as_markup(resize_keyboard = True)