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

pay_inkb1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Нажмите, чтобы оплатить тариф', 
                                                                       callback_data="buy_1")]])

pay_inkb2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Нажмите, чтобы оплатить тариф', 
                                                                       callback_data="buy_2")]])

pay_inkb3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Нажмите, чтобы оплатить тариф', 
                                                                       callback_data="buy_3")]])

