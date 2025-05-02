from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from src.settings import settings

redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
storage = RedisStorage(redis)

bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(link_preview_is_disabled=True, parse_mode='HTML'))
dp = Dispatcher(storage=storage)
