from aiogram.fsm.state import State, StatesGroup

class Get_data(StatesGroup):
    lesson =State()
    course = State()
    edit = State()
