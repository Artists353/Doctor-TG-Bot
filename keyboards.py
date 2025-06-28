from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

tariffs_kb = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Тарифы")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )

agree_kb = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Согласиться")],
            [KeyboardButton(text="Не соглашаться")]
        ],
        resize_keyboard=True
    )

pay_inkb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Оплата тарифа', 
                                                                       url='https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4')]])