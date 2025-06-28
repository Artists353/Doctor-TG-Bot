from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

tariffs_kb = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Тарифы")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

agree_kb = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Согласиться")],
            [KeyboardButton(text="Не соглашаться")]
        ],
        resize_keyboard=True,
        
    )

pay_inkb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Оплата тарифа', callback_data='Buy_tariff')]])