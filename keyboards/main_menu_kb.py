# keyboards/main_menu_kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_main_menu_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text='Расписания'),
            KeyboardButton(text='Оценки'),
            KeyboardButton(text='Погода')
        ],
        [
            KeyboardButton(text='Настройки')
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
