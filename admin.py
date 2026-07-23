from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ADMIN_ID = 8369041514



def is_admin(user_id):

    return user_id == ADMIN_ID



def admin_menu():

    keyboard = InlineKeyboardMarkup(
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
                    text="🎁 ساخت ووچر",
                    callback_data="create_voucher"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📋 لیست ووچرها",
                    callback_data="voucher_list"
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
                    text="⚙ تنظیمات",
                    callback_data="settings"
                )
            ]

        ]
    )

    return keyboard
