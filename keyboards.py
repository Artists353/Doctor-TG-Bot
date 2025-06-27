from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def tariffs_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Тарифы")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )

def agree_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Согласиться")],
            [KeyboardButton(text="Не соглашаться")]
        ],
        resize_keyboard=True
    )