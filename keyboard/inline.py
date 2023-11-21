from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, SwitchInlineQueryChosenChat

basic_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Basic Button', callback_data='basic'),
            InlineKeyboardButton(text='URL Button', url='https://github.com/'),
            InlineKeyboardButton(text='WebApp Button', web_app=WebAppInfo(url='https://fklska.slava111003.repl.co/')),
        ],
        [
            InlineKeyboardButton(
                text='SwitchInlineQuery (SIQ)',
                switch_inline_query='test'
            ),
            InlineKeyboardButton(
                text='SIQ in chosen chat',
                switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
                    query='test',
                    allow_bot_chats=True,
                )
            ),
            InlineKeyboardButton(
                text='SIQ in current chat',
                switch_inline_query_current_chat='test'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Profile',
                url='tg://user?id=6764625844'
            )
        ],
        [
            InlineKeyboardButton(
                text='Edit this message',
                callback_data='edit'
            ),
            InlineKeyboardButton(
                text='Show alert',
                callback_data='alert'
            ),
            InlineKeyboardButton(
                text='Show modal alert',
                callback_data='modal'
            )
        ]
    ]
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Back',
                callback_data='back'
            )
        ]
    ]
)