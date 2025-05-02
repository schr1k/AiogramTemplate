from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from src.settings import settings

subscribe = InlineKeyboardButton(text='✅ Подписаться', url=settings.CHANNEL_URL)
subscribe_kb = InlineKeyboardBuilder(
    [
        [subscribe],
    ],
).as_markup()
