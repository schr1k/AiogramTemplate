from aiogram import Router
from aiogram.filters import invert_f
from aiogram.types import CallbackQuery, Message

from src import kb
from src.filters import UsernameSetCall, UsernameSetMessage, UserSubscribedCall, UserSubscribedMessage

checks_router = Router()


@checks_router.message(invert_f(UserSubscribedMessage()))
async def not_subscribed_message(message: Message) -> None:
    await message.answer(text='Сначала подпишитесь на наш канал.', reply_markup=kb.subscribe_kb)


@checks_router.callback_query(invert_f(UserSubscribedCall()))
async def not_subscribed_call(call: CallbackQuery) -> None:
    await call.message.edit_text(text='Сначала подпишитесь на наш канал.', reply_markup=kb.subscribe_kb)


@checks_router.message(invert_f(UsernameSetMessage()))
async def username_not_set_message(message: Message) -> None:
    await message.answer(text='Для продолжения заполните юзернейм в настройках телеграм.')


@checks_router.callback_query(invert_f(UsernameSetCall()))
async def username_not_set_call(call: CallbackQuery) -> None:
    await call.message.edit_text(text='Для продолжения заполните юзернейм в настройках телеграм.')
