from aiogram.dispatcher.filters.state import State, StatesGroup

class All_states(StatesGroup):
    change_lang = State()
    change_foods = State()
    product_count = State()
    user_info = State()
