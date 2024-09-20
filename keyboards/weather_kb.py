from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_weekdays_kb():
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for day in weekdays:
        kb.add(KeyboardButton(day))
    return kb
