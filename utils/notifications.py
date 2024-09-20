# utils/notifications.py

import asyncio
from aiogram import Bot
from utils.db import get_parents_with_children, get_grades_report
from utils.logger import logger

async def send_notifications(bot: Bot):
    while True:
        await asyncio.sleep(86400)  # Запускать раз в сутки
        try:
            parents = get_parents_with_children()
            for parent_id, child_id in parents:
                report = get_grades_report(child_id)
                await bot.send_message(parent_id, report)
        except Exception as e:
            logger.error(f"Error sending notifications: {e}")
