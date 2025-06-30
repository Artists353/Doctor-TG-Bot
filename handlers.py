from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, PreCheckoutQuery, LabeledPrice, CallbackQuery
from aiogram.client.default import DefaultBotProperties

from keyboards import agree_kb
from keyboards import tariffs_kb
from keyboards import pay_inkb
from bot import Bot
router = Router()

CURRENCY = "RUB"
PROVIDER_TOKEN = "s"

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Добро пожаловать 🔹\n" \
    "📽 Здесь вы найдёте авторские видеоматериалы от опытного инструктора ЛФК, разработанные специально для:\n" \
    "— восстановления после травм и заболеваний\n" \
    "— мягкой гимнастики при болях\n" \
    "— поддержания подвижности в любом возрасте\n\n" \
    " 🛒 Вы можете:\n" \
    "• выбрать нужный курс\n" \
    "• оплатить прямо здесь\n" \
    "• получить доступ к видео сразу после оплаты\n\n" \
    "👩‍⚕️ Если не знаете, с чего начать — напишите нам, мы поможем подобрать подходящий материал.\n\n" \
    "Готовы начать? Нажмите Согласиться\n", 
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


@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.callback_query()
async def process_callback_query(callback_query: types.CallbackQuery, bot: Bot) -> None:
    prices = []
    description = 'Купить тариф.'
    prices = [LabeledPrice(label="Оплата тарифа: ", amount=100)]
    
    if prices:
        await bot.send_invoice(
            chat_id=callback_query.from_user.id,
            title='Покупка Тарифа',
            description=description,
            provider_token=PROVIDER_TOKEN,
            prices=prices,
            currency=CURRENCY
        )


@router.message(F.successful_payment)
async def process_successful_payment(message: Message) -> None:
    payload_to_message = {'Тариф'}
    response_message = payload_to_message.get(message.successful_payment.invoice_payload, "Оплата успешна!")
    await message.answer(response_message)


@router.message(lambda message: message.text and message.text.lower() == "не соглашаться")
async def answer_disagree(message: Message):
    await message.answer("К сожалению, без соглашения мы не можем предоставить вам доступ к материалу.", reply_markup=agree_kb)

@router.message(lambda message: message.text and message.text.lower() == "назад")
async def answer_disagree(message: Message):
    await message.answer("Вы вернулись к соглашению с правилами.", reply_markup=agree_kb)