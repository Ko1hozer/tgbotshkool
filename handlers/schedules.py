# handlers/schedules.py

from aiogram import types, Dispatcher
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.schedules_kb import get_schedules_kb
from keyboards.weekdays_kb import get_weekdays_kb
from keyboards.notifications_kb import get_notifications_kb
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from utils.db import save_schedule_to_db, delete_schedule_from_db, get_user_schedules
from keyboards.delete_schedule_kb import get_delete_schedule_kb
from utils.logger import logger

class ScheduleForm(StatesGroup):
    type = State()
    day = State()
    subject = State()
    start_time = State()
    end_time = State()
    notification = State()

async def schedules_handler(message: types.Message):
    schedules_kb = get_schedules_kb()
    await message.answer('Выберите действие с расписанием:', reply_markup=schedules_kb)

async def add_schedule(message: types.Message, state: FSMContext):
    await state.set_state(ScheduleForm.type)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Школьные занятия'), KeyboardButton(text='Дополнительные занятия')]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите тип занятия:", reply_markup=kb)

async def process_type(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text, user_id=message.from_user.id)
    await state.set_state(ScheduleForm.day)
    await message.answer("Выберите день недели:", reply_markup=get_weekdays_kb())

async def process_day(message: types.Message, state: FSMContext):
    await state.update_data(day=message.text)
    await state.set_state(ScheduleForm.subject)
    await message.answer("Введите название предмета:", reply_markup=ReplyKeyboardRemove())

async def process_subject(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await state.set_state(ScheduleForm.start_time)
    await message.answer("Введите время начала занятия (например, 09:00):")

async def process_start_time(message: types.Message, state: FSMContext):
    await state.update_data(start_time=message.text)
    await state.set_state(ScheduleForm.end_time)
    await message.answer("Введите время окончания занятия (например, 10:00):")

async def process_end_time(message: types.Message, state: FSMContext):
    await state.update_data(end_time=message.text)
    await state.set_state(ScheduleForm.notification)
    await message.answer("Выберите время напоминания:", reply_markup=get_notifications_kb())

async def process_notification(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data['notification'] = message.text
    save_schedule_to_db(data)
    await state.clear()
    await message.answer("Расписание сохранено!", reply_markup=ReplyKeyboardRemove())

async def delete_schedule(message: types.Message):
    delete_kb = await get_delete_schedule_kb(message.from_user.id)
    if delete_kb:
        await message.answer("Выберите расписание для удаления:", reply_markup=delete_kb)
    else:
        await message.answer("У вас нет расписаний для удаления.")

async def process_delete_callback(callback_query: CallbackQuery):
    schedule_id = callback_query.data.split('_')[1]
    delete_schedule_from_db(schedule_id)
    await callback_query.answer("Расписание удалено.")
    await callback_query.message.delete()

def register_handlers_schedules(dp: Dispatcher):
    dp.message.register(schedules_handler, Text(text='Расписания'))
    dp.message.register(add_schedule, Text(text='Ввести расписание'))
    dp.message.register(process_type, ScheduleForm.type)
    dp.message.register(process_day, ScheduleForm.day)
    dp.message.register(process_subject, ScheduleForm.subject)
    dp.message.register(process_start_time, ScheduleForm.start_time)
    dp.message.register(process_end_time, ScheduleForm.end_time)
    dp.message.register(process_notification, ScheduleForm.notification)
    dp.message.register(delete_schedule, Text(text='Удалить занятие'))
    dp.callback_query.register(process_delete_callback, lambda c: c.data and c.data.startswith('delete_'))
