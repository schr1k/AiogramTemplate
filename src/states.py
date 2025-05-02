from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    initials = State()
