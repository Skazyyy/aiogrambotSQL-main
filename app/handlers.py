import datetime
import app.keyboards as kb
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from app.states import Get_data
from app.database.pushes import push

router = Router()

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! выберите сегмент:", reply_markup=kb.start)
    await state.set_state(Get_data.lesson)

@router.message(Get_data.lesson)
async def get_lesson(message: Message, state: FSMContext):
    await state.update_data(lesson = message.text)
    await message.answer("Выберите курс", reply_markup=await kb.course(True if message.text == "Digital Skills" else False))
    await state.set_state(Get_data.course)

@router.message(Get_data.course)
async def get_course(message: Message, state: FSMContext):
    await state.update_data(course = message.text)
    await message.answer("введите текст опечатки", reply_markup=kb.delete)
    await state.set_state(Get_data.edit)

@router.message(Get_data.edit)
async def get_course(message: Message, state: FSMContext):
    await state.update_data(edit = message.text)
    data = await state.get_data()
    push(str(datetime.datetime.now())[:-10], message.from_user.first_name, data['lesson'], data['course'], data['edit'])
    await message.answer("Ваша опечатка сохранена", reply_markup=kb.delete)
    await state.clear()