# keyboards/notifications_kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_notifications_kb() -> ReplyKeyboardMarkup:
    options = ['1 час', '1.5 часа', '2 часа', 'Без напоминаний']
    keyboard = [[KeyboardButton(text=option)] for option in options]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
