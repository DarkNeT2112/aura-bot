from aiogram import types

from keyboards.inline.foods import foods_dont_garnier
from loader import dp
# for change leng funtion
from states.all_states import All_states


# uzga langa def
@dp.message_handler(text="🇺🇿 Uz",state=All_states.change_lang)
async def for_uz_lang(msg : types.Message):
    change_leng = 'uz'
    await msg.bot.send_photo(chat_id=msg.chat.id,
        caption="📖 Menyular",photo="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Nnx8fGVufDB8fHx8&w=1000&q=80",
        reply_markup=foods_dont_garnier)
    await All_states.change_foods.set()
#
# ruga langa def
@dp.message_handler(text="🇷🇺 Ru",state=All_states.change_lang)
async def for_ru_lang(msg : types.Message):
    change_leng = "ru"
    await msg.answer("Menyu for ruscha",reply_markup=foods_dont_garnier)
    await All_states.change_foods.set()

