from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎁 دریافت ووچر",
                    callback_data="get_voucher"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💰 موجودی من",
                    callback_data="balance"
                ),
                InlineKeyboardButton(
                    text="🛒 خرید اشتراک",
                    callback_data="buy"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📜 سفارش‌های من",
                    callback_data="orders"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👥 دعوت دوستان",
                    callback_data="invite"
                )
            ],

            [
                InlineKeyboardButton(
                    text="☎️ پشتیبانی",
                    callback_data="support"
                )
            ]

        ]
    )

    return keyboard



def admin_menu():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📊 آمار ربات",
                    callback_data="stats"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👥 کاربران",
                    callback_data="users"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎁 مدیریت ووچر",
                    callback_data="voucher_manage"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💳 پرداخت‌ها",
                    callback_data="payments"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📢 پیام همگانی",
                    callback_data="broadcast"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⬅️ برگشت",
                    callback_data="back"
                )
            ]

        ]
    )

    return keyboard
