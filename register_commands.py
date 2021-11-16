from aiogram import types
from connector import dp
from states import WaitFor
from keyboard import *
from aiogram.types.message import ContentType


@dp.message_handler(content_types=ContentType.TEXT, state=WaitFor.waiting_for_name)
async def unknown_message(msg: types.Message):
    name = msg.text
    print(name)
    await msg.reply("Thanks! \nNow please write the year of your birth.", reply_markup=kb_help)
    await WaitFor.waiting_for_age.set()


@dp.message_handler(content_types=ContentType.TEXT, state=WaitFor.waiting_for_age)
async def unknown_message(msg: types.Message):
    year = msg.text
    print(year)
    await msg.reply("Thanks! \nNow please write the place where you are currently located", reply_markup=kb_help)
    await WaitFor.waiting_for_city.set()


@dp.message_handler(content_types=ContentType.TEXT, state=WaitFor.waiting_for_city)
async def unknown_message(msg: types.Message):
    city = msg.text
    print(city)
    await msg.reply("Thanks! \nNow please write your gender", reply_markup=kb_help)
    await WaitFor.waiting_for_gender.set()


@dp.message_handler(content_types=ContentType.TEXT, state=WaitFor.waiting_for_gender)
async def unknown_message(msg: types.Message):
    gender = msg.text
    print(gender)
    await msg.reply("Thanks! Now we are done with this! \nI know more about your personality, but I still need to "
                    "collect some books that you like! \nIf you would like to change your contact information "
                    "you can do it at any time with /change_contact_info button",
                    reply_markup=kb_tell_and_help_and_change_contact_info)
    await WaitFor.waiting_for_books.set()


@dp.message_handler(commands=['change_contact_info'], state=[WaitFor.free_state, WaitFor.waiting_for_books])
async def process_start_command(message: types.Message):
    await message.reply("Which info would you like to change?", reply_markup=kb_change_contact_info)
    await WaitFor.changing_contact_info.set()


@dp.message_handler(commands=['change_name'], state=WaitFor.changing_contact_info)
async def process_start_command(message: types.Message):
    await message.reply("Write your new name:")
    await WaitFor.waiting_for_name.set()


@dp.message_handler(commands=['change_age'], state=WaitFor.changing_contact_info)
async def process_start_command(message: types.Message):
    await message.reply("Write your new year of birth:")
    await WaitFor.waiting_for_age().set()


@dp.message_handler(commands=['change_city'], state=WaitFor.changing_contact_info)
async def process_start_command(message: types.Message):
    await message.reply("Write a new city of your location:")
    await WaitFor.waiting_for_city().set()


@dp.message_handler(commands=['change_gender'], state=WaitFor.changing_contact_info)
async def process_start_command(message: types.Message):
    await message.reply("Write your new gender:")
    await WaitFor.waiting_for_gender().set()
