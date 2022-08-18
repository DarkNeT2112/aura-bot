from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

from data.foods import befstragov, mysa_gribami, kotlet_govyaji, kotlet_kurrini, pasta_karaban, pasta_alferedo, \
    otbivnaya_govyaji, otbivnaya_kurinni, kotlet_po_kivisiy, nagetsi_sfri, kuridsa_sovoshami, kuridsa_gribami, \
    myasa_podomashni, myasa_po_kitay

# foods menu
foods_dont_garnier =InlineKeyboardMarkup(row_width=1)
foods_dont_garnier.insert(InlineKeyboardButton(text=f'{befstragov["name"]}',callback_data=f'{befstragov["name"]}'))
foods_dont_garnier.insert(InlineKeyboardButton(text=f'{mysa_gribami["name"]}',callback_data=f'{mysa_gribami["name"]}'))
foods_dont_garnier.insert(InlineKeyboardButton(text=f'{myasa_po_kitay["name"]}',callback_data=f'{myasa_po_kitay["name"]}'))
foods_dont_garnier.insert(InlineKeyboardButton(text=f'{myasa_podomashni["name"]}',callback_data=f'{myasa_podomashni["name"]}'))
foods_dont_garnier.insert(InlineKeyboardButton(text=f'{kuridsa_gribami["name"]}',callback_data=f'{kuridsa_gribami["name"]}'))
foods_dont_garnier.insert(InlineKeyboardButton(text=f'{kuridsa_sovoshami["name"]}',callback_data=f'{kuridsa_sovoshami["name"]}'))
foods_dont_garnier.insert(InlineKeyboardButton(text=f'{nagetsi_sfri["name"]}',callback_data=f'{nagetsi_sfri["name"]}'))
foods_dont_garnier.insert(InlineKeyboardButton(text=f'📖 Boshqa ovqatlar',callback_data="boshqa_ovqatlar"))

# foods menu
foods_dont_garnier_2 = InlineKeyboardMarkup(row_width=1)
foods_dont_garnier_2.insert(InlineKeyboardButton(text=f'{kotlet_po_kivisiy["name"]}',callback_data=f'{kotlet_po_kivisiy["name"]}'))
foods_dont_garnier_2.insert(InlineKeyboardButton(text=f'{otbivnaya_kurinni["name"]}',callback_data=f'{otbivnaya_kurinni["name"]}'))
foods_dont_garnier_2.insert(InlineKeyboardButton(text=f'{otbivnaya_govyaji["name"]}',callback_data=f'{otbivnaya_govyaji["name"]}'))
foods_dont_garnier_2.insert(InlineKeyboardButton(text=f'{pasta_alferedo["name"]}',callback_data=f'{pasta_alferedo["name"]}'))
foods_dont_garnier_2.insert(InlineKeyboardButton(text=f'{pasta_karaban["name"]}',callback_data=f'{pasta_karaban["name"]}'))
foods_dont_garnier_2.insert(InlineKeyboardButton(text=f'{kotlet_kurrini["name"]}',callback_data=f'{kotlet_kurrini["name"]}'))
foods_dont_garnier_2.insert(InlineKeyboardButton(text=f'{kotlet_govyaji["name"]}',callback_data=f'{kotlet_govyaji["name"]}'))

