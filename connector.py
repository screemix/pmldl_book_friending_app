from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '2141280047:AAHsAq3iDUQ9rSRyy43BQV0rzgsHp55Uq-M'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())