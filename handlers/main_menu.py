# handlers/main_menu.py

from aiogram import types, Dispatcher
from aiogram.filters import Command
from keyboards.main_menu_kb import get_main_menu_kb
from utils.logger import logger

async def start_handler(message: types.Message):
    logger.info(f'User {message.from_user.id} started the bot.')
    main_menu_kb = get_main_menu_kb()
    await message.answer('Добро пожаловать! Выберите нужный раздел из меню ниже.', reply_markup=main_menu_kb)

def register_handlers_main_menu(dp: Dispatcher):
    dp.message.register(start_handler, Command(commands=['start']))
