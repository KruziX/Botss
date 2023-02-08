# Слито в https://t.me/HACKER_PHONE_VIP

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Слито в https://t.me/HACKER_PHONE_VIP

def menu_kb():
    button1 = KeyboardButton('📥 Загрузить файл')
    button2 = KeyboardButton('🌸 Мои файлы')
    menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_kb.add(button1)
    menu_kb.add(button2)
    return menu_kb

# Слито в https://t.me/HACKER_PHONE_VIP

def back_kb():
    button1 = KeyboardButton('🚫 Отмена')
    back_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    back_kb1.add(button1)
    return back_kb1

# Слито в https://t.me/HACKER_PHONE_VIP

def delete_file():
    markup = InlineKeyboardMarkup()
    btn2 = InlineKeyboardButton(text='⚡ Удалить файл', callback_data=f'delete_file')
    markup.add(btn2)
    return markup

# Слито в https://t.me/HACKER_PHONE_VIP

def delete_back():
    markup = InlineKeyboardMarkup()
    btn2 = InlineKeyboardButton(text='🚫 Отмена', callback_data=f'delete_back')
    markup.add(btn2)
    return markup

# Слито в https://t.me/HACKER_PHONE_VIP