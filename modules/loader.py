from aiogram import Bot, Dispatcher

from config import TOKEN
from modules.commands import main_router


bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(main_router)
