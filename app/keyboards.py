from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

delete = ReplyKeyboardRemove()

start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Русский язык')],
        [KeyboardButton(text='Математика')],
        [KeyboardButton(text='Информатика')],
        [KeyboardButton(text='Физика')],
        [KeyboardButton(text='История')],#
        [KeyboardButton(text='Обществознание')],#
        [KeyboardButton(text='Английский язык')],#
        [KeyboardButton(text='Биология')],#
        [KeyboardButton(text='Химия')],#
        [KeyboardButton(text='Digital Skills')]
    ], resize_keyboard=True, one_time_keyboard=True
)

async def course(is_digital_skills: bool):
    kb = ReplyKeyboardBuilder()
    if is_digital_skills:
        kb.add(KeyboardButton(text='Программирование')).add(KeyboardButton(text='Графический дизайн')).add(KeyboardButton(text='Маркетинг'))
        return kb.adjust(1).as_markup()
    kb.add(KeyboardButton(text='8 класс')).add(KeyboardButton(text='9 класс')).add(KeyboardButton(text='10 класс')).add(KeyboardButton(text='11 класс'))
    return kb.adjust(1).as_markup()
