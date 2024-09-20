# keyboards/grades_kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_grades_kb() -> ReplyKeyboardMarkup:
    grades = ['5', '4', '3', '2']
    keyboard = [[KeyboardButton(text=grade)] for grade in grades]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
