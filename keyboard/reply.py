from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, WebAppInfo


reply_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Common Keyboard button'
            ),
            KeyboardButton(
                text='WebApp Keyboard button',
                web_app=WebAppInfo(url='https://github.com/')
            )
        ],
        [
            KeyboardButton(
                text='Send contact',
                request_contact=True,
            ),
            KeyboardButton(
                text='Send location',
                request_location=True
            ),
            KeyboardButton(
                text='Send poll',
                request_poll=KeyboardButtonPollType(),
            ),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Reply Keyboard buttons'
)
