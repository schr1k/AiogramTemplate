import asyncio
import logging

from src.bot import bot, dp
from src.routers.checks import checks_router
from src.routers.system import system_router
from src.routers.users import users_router

logging.basicConfig(level=logging.INFO)

dp.include_router(checks_router)
dp.include_router(system_router)
dp.include_router(users_router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
