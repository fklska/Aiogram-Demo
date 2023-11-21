from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='help',
            description='Show basic comands'
        ),
        BotCommand(
            command='start',
            description='Run the bot'
        ),
        BotCommand(
            command='inline',
            description='show capabilities of inline buttons'
        ),
        BotCommand(
            command='reply',
            description='show capabilities of reply buttons'
        ),
        BotCommand(
            command='pay',
            description='Send the test Invoice'
        ),
        BotCommand(
            command='location',
            description='Send the random Location'
        ),
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )
