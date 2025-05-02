from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

users_router = Router()


@users_router.message(Command('start'))
async def start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(text=f'Привет, {message.from_user.first_name}')
