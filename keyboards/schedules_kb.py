# keyboards/schedules_kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_schedules_kb() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text='Ввести расписание'),
            KeyboardButton(text='Редактировать расписание')
        ],
        [
            KeyboardButton(text='Удалить занятие'),
            KeyboardButton(text='Назад')
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
