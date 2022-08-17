from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.change_lang import lang
from loader import dp
from states.all_states import All_states


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} !",reply_markup=lang)
    await All_states.change_lang.set()
