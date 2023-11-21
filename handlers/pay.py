from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram import Bot
import os


async def send_invoice(message: Message, bot: Bot):
    await message.answer_invoice(
        title='Счет на оплату',
        description='Тестовый счет на оплату',
        payload='Test Payload',
        provider_token=os.getenv('PAY'),
        currency='rub',
        prices=[
            LabeledPrice(
                label='Основной товар',
                amount=50000
            ),
            LabeledPrice(
                label='НДС',
                amount=10000,
            )
        ],
        max_tip_amount=150000,
        suggested_tip_amounts=[10000, 20000, 50000],
        start_parameter='yes',
        photo_url='https://i.imgur.com/zh4IXz5.gif',
        photo_size=100,
        photo_height=400,
        photo_width=400,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=True,
        is_flexible=True
    )


async def pre_checked_auery(bot: Bot, pre_chekout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_chekout_query.id, ok=True)
