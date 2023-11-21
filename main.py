import asyncio
import os

from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.utils import markdown
from dotenv import load_dotenv

from handlers.basic import (get_information, read_contact, read_location,
                            send_location, show_inline, show_reply)
from handlers.callback import callback
from handlers.pay import send_invoice
from utils.commands import set_commands

load_dotenv()

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await set_commands(message.bot)
    await message.answer(text=f"<code>Hello, {markdown.code(message.from_user.first_name)}!</code>")
    await message.reply(text=f"<tg-spoiler>Hello, {markdown.code(message.from_user.last_name)}!</tg-spoiler>")


async def main():
    bot = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    dp.message.register(show_inline, Command(commands=['inline']))
    dp.message.register(show_reply, Command(commands=['reply']))
    dp.message.register(send_invoice, Command(commands=['pay']))
    dp.message.register(send_location, Command(commands=['location']))
    dp.message.register(read_contact, F.contact)
    dp.message.register(read_location, F.location)
    dp.my_chat_member.register(get_information)
    #dp.chat_member.register(get_information)
    dp.callback_query.register(callback)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
