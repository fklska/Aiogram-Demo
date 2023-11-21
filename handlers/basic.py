from aiogram.types import Message, ChatMemberUpdated
from keyboard.inline import basic_markup
from aiogram import Bot
from keyboard.reply import reply_markup
from random import randint


async def get_information(event: ChatMemberUpdated, bot: Bot):
    #print(message.json())
    print(event.json())


async def show_inline(message: Message):
    await message.answer(
        text='Разновидности inline кнопок',
        reply_markup=basic_markup
    )


async def show_reply(message: Message, bot: Bot):
    await message.answer(
        text='Reply кнопки',
        reply_markup=reply_markup
    )


async def read_contact(message: Message, bot: Bot):
    await message.answer(
        f'Получен контакт: \n number: {message.contact.phone_number} \n Name: {message.contact.first_name} \n user_id: {message.contact.user_id} \n vcard: {message.contact.vcard}'
    )


async def read_location(message: Message, bot: Bot):
    await message.answer(
        f'Получена локация \n Долгота: {message.location.longitude} \n Широта: {message.location.latitude}'
    )


async def send_location(message: Message):
    await message.answer_location(
        latitude=float(randint(1, 100)),
        longitude=float(randint(1, 100))
    )