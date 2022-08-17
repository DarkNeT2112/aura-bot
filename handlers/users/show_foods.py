from aiogram import types
from keyboards.inline.foods import foods_button, foods
from loader import dp, bot
# for change leng funtion
from states.all_states import All_states


def change_leng():
    leng = ""

# uzga langa def
@dp.message_handler(text="🇺🇿 Uz",state=All_states.change_lang)
async def for_uz_lang(msg : types.Message):
    change_leng = 'uz'
    await msg.bot.send_photo(chat_id=msg.chat.id,reply_markup=foods_button,caption="📖 Menyular",photo="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Nnx8fGVufDB8fHx8&w=1000&q=80")
    await All_states.change_foods.set()

# ruga langa def
@dp.message_handler(text="🇷🇺 Ru",state=All_states.change_lang)
async def for_ru_lang(msg : types.Message):
    change_leng = "ru"
    await msg.answer("Menyu for ruscha",reply_markup=foods_button)
    await All_states.change_foods.set()

# Tanlagan ovqatlar uchun javob berad
ids = []
for i in foods:
    ids.append(i["name"])
j=[]
@dp.callback_query_handler(text=ids,state=All_states.change_foods)
async def show_food_info(call : types.CallbackQuery):
    global i, j
    for i in foods:
        if i["name"]==call.data:
            j = i
    # hato rasimda bogan ekan rasmni jonatsa boldi end
    await call.bot.send_photo(chat_id=call.message.chat.id,photo=j["image"],caption=f"{j['discribtion']} {j['name']}")

# orqaga button uchun function
# @dp.callback_query_handler(text="orqaga",state=All_states.change_foods)
# async def for_back(call : types.CallbackQuery):
#     await call.message.answer("Orqaga",reply_markup=foods_button)
#     await All_states.change_foods.set()
#