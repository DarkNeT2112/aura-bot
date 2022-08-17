from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
food = {
    "name" : "Borsh",
    "image" : "https://img.freepik.com/premium-photo/big-hamburger-with-double-beef-french-fries_252907-8.jpg?w=2000",
    "cost": "20 000",
    "discribtion" : "Savbzi kartoshka"
}
food1 = {
    "name" : "Mastava",
    "image" : "https://img.freepik.com/premium-photo/big-hamburger-with-double-beef-french-fries_252907-8.jpg?w=2000",
    "cost": "20 000",
    "discribtion" : "Savbzi kartoshka"
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
    "discribtion" : "Savbzi kartoshka"
}

foods = []

foods.append(food1)
foods.append(food2)
foods.append(food3)
foods.append(food)
# print(foods)
# ovqatlar uchun button
foods_button = InlineKeyboardMarkup(row_width=2)
for i in foods:
    foods_button.insert(InlineKeyboardButton(text="🔹 "+i["name"],callback_data=i["name"]))
# foods_button.insert(InlineKeyboardButton(text="🔙 Orqaga",callback_data="orqaga"))

