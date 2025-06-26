from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def kb_agree():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Согласиться")],
            [KeyboardButton(text="Не соглашаться")]
        ],
        resize_keyboard=True
    )