from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    kb = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎁 خرید ووچر",
                    callback_data="buy"
                ),
                InlineKeyboardButton(
                    text="💰 موجودی من",
                    callback_data="balance"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📦 سفارشات من",
                    callback_data="orders"
                ),
                InlineKeyboardButton(
                    text="👤 حساب کاربری",
                    callback_data="profile"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💎 شارژ حساب",
                    callback_data="charge"
                ),
                InlineKeyboardButton(
                    text="🆘 پشتیبانی",
                    callback_data="support"
                )
            ]

        ]
    )


    return kb



def products_menu():

    kb = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="⭐ تلگرام پریمیوم ۱ ماهه",
                    callback_data="premium_1"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⭐ تلگرام پریمیوم ۳ ماهه",
                    callback_data="premium_3"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⭐ تلگرام پریمیوم ۶ ماهه",
                    callback_data="premium_6"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🔙 بازگشت",
                    callback_data="back"
                )
            ]

        ]
    )

    return kb
