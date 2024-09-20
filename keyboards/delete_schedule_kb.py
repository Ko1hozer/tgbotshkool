# keyboards/delete_schedule_kb.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db import get_user_schedules

async def get_delete_schedule_kb(user_id):
    schedules = get_user_schedules(user_id)
    if not schedules:
        return None
    kb = InlineKeyboardMarkup()
    for sched in schedules:
        button = InlineKeyboardButton(text=f"{sched['subject']} {sched['day_of_week']}", callback_data=f"delete_{sched['id']}")
        kb.add(button)
    return kb
