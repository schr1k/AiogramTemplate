from aiogram.enums import ChatMemberStatus
from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message

from src.bot import bot
from src.settings import settings


class UserSubscribedMessage(Filter):
    async def __call__(self, message: Message) -> bool:
        member = await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=message.from_user.id)
        return member.status != ChatMemberStatus.LEFT


class UserSubscribedCall(Filter):
    async def __call__(self, call: CallbackQuery) -> bool:
        member = await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=call.from_user.id)
        return member.status != ChatMemberStatus.LEFT


class UsernameSetMessage(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.username is not None


class UsernameSetCall(Filter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return call.from_user.username is not None
