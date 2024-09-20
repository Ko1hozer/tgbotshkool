# keyboards/settings_kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_settings_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text='Изменить расписание')],
        [KeyboardButton(text='Включить оповещение')],
        [KeyboardButton(text='Назад')]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
