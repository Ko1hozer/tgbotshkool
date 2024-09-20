# keyboards/subjects_kb.py

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from utils.db import get_subjects

def get_subjects_kb(user_id) -> ReplyKeyboardMarkup:
    subjects = get_subjects(user_id)
    if not subjects:
        subjects = ['Математика', 'Русский язык', 'Английский язык', 'История']  # Предложить стандартные предметы
    keyboard = [[KeyboardButton(text=subject)] for subject in subjects]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
