# handlers/parent.py

from aiogram import types, Dispatcher
from aiogram.filters import Command
from utils.db import save_invite_code, get_child_id_by_invite_code, link_parent_to_child
from utils.logger import logger
import uuid

async def generate_invite_link(message: types.Message):
    code = str(uuid.uuid4())
    save_invite_code(message.from_user.id, code)
    await message.answer(f"Передайте этот код родителю для привязки: {code}")

async def accept_invite_code(message: types.Message):
    code = message.text.strip()
    child_id = get_child_id_by_invite_code(code)
    if child_id:
        link_parent_to_child(message.from_user.id, child_id)
        await message.answer("Вы успешно привязаны к ребенку.")
    else:
        await message.answer("Неверный код. Попробуйте еще раз.")

def register_handlers_parent(dp: Dispatcher):
    dp.message.register(generate_invite_link, Command(commands=['add_parent']))
    dp.message.register(accept_invite_code, Command(commands=['accept_invite']))
