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
                    text="💎 محصولات پریمیوم",
                    callback_data="products"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💰 کیف پول",
                    callback_data="wallet"
                ),
                InlineKeyboardButton(
                    text="📦 سفارش‌های من",
                    callback_data="orders"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👤 حساب کاربری",
                    callback_data="profile"
                ),
                InlineKeyboardButton(
                    text="📊 موجودی",
                    callback_data="balance"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎧 پشتیبانی",
                    callback_data="support"
                )
            ]

        ]
    )



def admin_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="👑 مدیریت کاربران",
                    callback_data="manage_users"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎁 ارسال ووچر",
                    callback_data="send_voucher"
                ),
                InlineKeyboardButton(
                    text="📈 آمار فروش",
                    callback_data="stats"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⚙️ تنظیمات",
                    callback_data="settings"
                )
            ]

        ]
    )
