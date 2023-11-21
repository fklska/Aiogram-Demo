from aiogram.types import CallbackQuery
from aiogram import Bot
from keyboard.inline import back, basic_markup


async def callback(call: CallbackQuery, bot: Bot):
    data = call.data
    if data == 'edit':
        await call.message.edit_text(
            text='Edited message',
            reply_markup=back
        )

    elif data == 'back':
        await call.message.edit_text(
            text='Разновидности inline кнопок',
            reply_markup=basic_markup
        )

    elif data == 'alert':
        await call.answer(
            'Black Dissapeared alert'
        )

    elif data == 'modal':
        await call.answer(
            'Modal alert',
            show_alert=True
        )

    else:
        await call.message.answer(text='You press basic inline button')
        await call.answer(
            'You press basic inline button (Notification)'
        )
