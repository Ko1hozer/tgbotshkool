# keyboards/weekdays_kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_weekdays_kb() -> ReplyKeyboardMarkup:
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    keyboard = [[KeyboardButton(text=day)] for day in weekdays]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
