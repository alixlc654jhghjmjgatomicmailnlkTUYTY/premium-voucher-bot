from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ADMIN_ID = 8369041514


def is_admin(user_id):
    return user_id == ADMIN_ID



def admin_panel():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📊 آمار ربات",
                    callback_data="admin_stats"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👥 کاربران",
                    callback_data="admin_users"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💰 مدیریت موجودی",
                    callback_data="admin_balance"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎁 مدیریت ووچر",
                    callback_data="admin_voucher"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📦 سفارش‌ها",
                    callback_data="admin_orders"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📢 پیام همگانی",
                    callback_data="admin_broadcast"
                )
            ]

        ]
    )
