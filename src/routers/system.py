from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

system_router = Router()


@system_router.message(Command('gid'))
async def group_id(message: Message) -> None:
    await message.answer(text=str(message.chat.id))


@system_router.message(Command('id'))
async def user_id(message: Message) -> None:
    await message.answer(text=str(message.from_user.id))
