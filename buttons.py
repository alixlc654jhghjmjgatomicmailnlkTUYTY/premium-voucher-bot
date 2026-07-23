from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎁 خرید ووچر",
                    callback_data="buy"
                ),
                InlineKeyboardButton(
                    text="💰 کیف پول",
                    callback_data="balance"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💳 شارژ حساب",
                    callback_data="charge"
                ),
                InlineKeyboardButton(
                    text="📦 سفارشات من",
                    callback_data="orders"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👤 حساب کاربری",
                    callback_data="profile"
                ),
                InlineKeyboardButton(
                    text="🆘 پشتیبانی",
                    callback_data="support"
                )
            ]

        ]
    )




def charge_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="💵 50,000 تومان",
                    callback_data="charge_50000"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💵 100,000 تومان",
                    callback_data="charge_100000"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💵 500,000 تومان",
                    callback_data="charge_500000"
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




def products_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="⭐ پریمیوم 1 ماهه",
                    callback_data="premium_1"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⭐ پریمیوم 3 ماهه",
                    callback_data="premium_3"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⭐ پریمیوم 6 ماهه",
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
