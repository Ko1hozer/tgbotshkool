# bot.py

import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.main_menu import register_handlers_main_menu
from handlers.schedules import register_handlers_schedules
from handlers.grades import register_handlers_grades
from handlers.weather import register_handlers_weather
from handlers.settings import register_handlers_settings
from handlers.parent import register_handlers_parent

from utils.db import init_db
from utils.notifications import send_notifications

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация обработчиков
    register_handlers_main_menu(dp)
    register_handlers_schedules(dp)
    register_handlers_grades(dp)
    register_handlers_weather(dp)
    register_handlers_settings(dp)
    register_handlers_parent(dp)

    # Инициализация базы данных
    init_db()

    # Запуск фоновой задачи отправки уведомлений
    asyncio.create_task(send_notifications(bot))

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
