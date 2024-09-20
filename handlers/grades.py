# handlers/grades.py

from aiogram import types, Dispatcher
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.grades_kb import get_grades_kb
from keyboards.subjects_kb import get_subjects_kb
from utils.db import save_grade_to_db
from aiogram.types import ReplyKeyboardRemove
from utils.logger import logger

class GradeForm(StatesGroup):
    subject = State()
    grade = State()
    photo = State()

async def grades_handler(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Внести оценки'), KeyboardButton(text='Сколько я заработал(а)')],
            [KeyboardButton(text='Назад')]
        ],
        resize_keyboard=True
    )
    await message.answer('Выберите действие с оценками:', reply_markup=kb)

async def add_grade(message: types.Message, state: FSMContext):
    await state.set_state(GradeForm.subject)
    await message.answer("Выберите предмет:", reply_markup=get_subjects_kb(message.from_user.id))

async def process_subject(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await state.set_state(GradeForm.grade)
    await message.answer("Выберите оценку:", reply_markup=get_grades_kb())

async def process_grade(message: types.Message, state: FSMContext):
    await state.update_data(grade=int(message.text))
    await state.set_state(GradeForm.photo)
    await message.answer("Пришлите фотографию оценки.", reply_markup=ReplyKeyboardRemove())

async def process_photo(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.answer("Пожалуйста, пришлите фотографию.")
        return
    data = await state.get_data()
    photo_id = message.photo[-1].file_id
    save_grade_to_db(message.from_user.id, data['subject'], data['grade'], photo_id)
    await state.clear()
    await message.answer("Оценка сохранена!")

def register_handlers_grades(dp: Dispatcher):
    dp.message.register(grades_handler, Text(text='Оценки'))
    dp.message.register(add_grade, Text(text='Внести оценки'))
    dp.message.register(process_subject, GradeForm.subject)
    dp.message.register(process_grade, GradeForm.grade)
    dp.message.register(process_photo, GradeForm.photo)
