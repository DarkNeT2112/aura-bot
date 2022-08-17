from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
food = {
    "name" : "Borsh",
    "image" : "https://img.freepik.com/premium-photo/big-hamburger-with-double-beef-french-fries_252907-8.jpg?w=2000",
    "cost": "20 000",
    "discribtion" : """1 — Qiymali bulg'or qalampiri 2 — Klyarda tayyorlangan tovuq sonchalari  3 — Ikki barobar ko'p garnir fri/makaronlar

35 000 so'm

💰Bitta porsiyasining narxi - 35.000 so'm💰

🚚 Yetkazib berish pulli!
(8 porsiyadan ko'pga buyurtma bersangiz, bepul yetkazib beramiz)

❗️ Buyurtma qabul qilamiz❗️
☎️99 130-02-20"""
}
food1 = {
    "name" : "Mastava",
    "image" : "https://img.freepik.com/premium-photo/big-hamburger-with-double-beef-french-fries_252907-8.jpg?w=2000",
    "cost": "20 000",
    "discribtion" : """1 — Qiymali bulg'or qalampiri 2 — Klyarda tayyorlangan tovuq sonchalari  3 — Ikki barobar ko'p garnir fri/makaronlar

35 000 so'm

💰Bitta porsiyasining narxi - 35.000 so'm💰

🚚 Yetkazib berish pulli!
(8 porsiyadan ko'pga buyurtma bersangiz, bepul yetkazib beramiz)

❗️ Buyurtma qabul qilamiz❗️
☎️99 130-02-20"""
}
food2 = {
    "name" : "Kasha",
    "image" : "https://st.depositphotos.com/1177973/1257/i/600/depositphotos_12574732-stock-photo-fast-food-isolated-on-white.jpg",
    "cost": "20 000",
    "discribtion" : "Savbzi kartoshka"
}
food3 = {
    "name" : "Myasa gribami",
    "image" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrIPch7cLf1c5n2ovgsW5xSF_tYDPHShR6j8bVCvlpQRj4Ps9xeZWDe8obC5wTFNuu0sg&usqp=CAU",
    "cost": "20 000",
    "discribtion" : """1 — Qiymali bulg'or qalampiri 2 — Klyarda tayyorlangan tovuq sonchalari  3 — Ikki barobar ko'p garnir fri/makaronlar

35 000 so'm

💰Bitta porsiyasining narxi - 35.000 so'm💰

🚚 Yetkazib berish pulli!
(8 porsiyadan ko'pga buyurtma bersangiz, bepul yetkazib beramiz)

❗️ Buyurtma qabul qilamiz❗️
☎️99 130-02-20"""
}
foods = []
foods.append(food1)
foods.append(food2)
foods.append(food3)
foods.append(food)

# ovqatlar uchun button
foods_button = InlineKeyboardMarkup(row_width=2)
for i in foods:
    foods_button.insert(InlineKeyboardButton(text="🔹 "+i["name"],callback_data=i["name"]))
# foods_button.insert(InlineKeyboardButton(text="🔙 Orqaga",callback_data="orqaga"))


# button for order
order = InlineKeyboardMarkup(row_width=3)
food_count = [1,2,3,4,5,6,7,8,9]

for i in food_count:
    order.insert(InlineKeyboardButton(text=f"+{i}", callback_data=f"{i}"))
order.insert(InlineKeyboardButton(text="🔙 Orqaga",callback_data="orqaga"))


# user order count food
user_order = InlineKeyboardMarkup(row_width=2)
user_order.insert(InlineKeyboardButton(text="-1",callback_data="minus"))
user_order.insert(InlineKeyboardButton(text="+1",callback_data="plus"))
user_order.insert(InlineKeyboardButton(text="🔙 Orqaga",callback_data="orqaga"))
user_order.insert(InlineKeyboardButton(text="🛒 Savatcha",callback_data="savatcha"))