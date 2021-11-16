from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_help = KeyboardButton('/help')
button_tell = KeyboardButton('/tell_about_me')
button_change_contact_info = KeyboardButton('/change_contact_info')
button_change_name = KeyboardButton('/change_name')
button_change_age = KeyboardButton('/change_age')
button_change_gender = KeyboardButton('/change_gender')
button_change_city = KeyboardButton('/change_city')
button_done = KeyboardButton('/done')


kb_help = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_help)
kb_tell_and_help = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_help).add(button_tell)
kb_tell_and_help_and_change_contact_info = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_help).add(button_tell).add(button_change_contact_info)
kb_change_contact_info = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_help).add(button_change_name).add(button_change_age)\
    .add(button_change_gender).add(button_change_city).add(button_done)
