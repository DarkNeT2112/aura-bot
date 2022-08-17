from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

# change lang buttons
lang = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text="🇺🇿 Uz"),
            KeyboardButton(text="🇷🇺 Ru")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


