# handlers/settings.py

from aiogram import types, Dispatcher
from aiogram.filters import Text
from keyboards.settings_kb import get_settings_kb
from utils.logger import logger

async def settings_handler(message: types.Message):
    settings_kb = get_settings_kb()
    await message.answer('Настройки:', reply_markup=settings_kb)

def register_handlers_settings(dp: Dispatcher):
    dp.message.register(settings_handler, Text(text='Настройки'))
