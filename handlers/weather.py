# handlers/weather.py

from aiogram import types, Dispatcher
from aiogram.filters import Text
from utils.weather_api import get_weather
from utils.logger import logger

async def weather_handler(message: types.Message):
    city = 'Москва'  # Вы можете добавить функционал для выбора города
    weather_info = get_weather(city)
    await message.answer(f'Погода в {city}:\n{weather_info}')

def register_handlers_weather(dp: Dispatcher):
    dp.message.register(weather_handler, Text(text='Погода'))
