from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# =========================
# منوی اصلی کاربر
# =========================

def main_menu():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="💎 خرید ووچر",
                    callback_data="buy_voucher"
                )
            ],


            [
                InlineKeyboardButton(
                    text="💰 کیف پول من",
                    callback_data="wallet"
                ),

                InlineKeyboardButton(
                    text="📦 سفارش‌های من",
                    callback_data="orders"
                )
            ],


            [
                InlineKeyboardButton(
                    text="🎁 کد تخفیف",
                    callback_data="discount"
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





# =========================
# انتخاب محصول
# =========================


def products_menu():


    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[


            [
                InlineKeyboardButton(
                    text="💵 ووچر 10 دلاری",
                    callback_data="voucher_10"
                )
            ],


            [
                InlineKeyboardButton(
                    text="💵 ووچر 25 دلاری",
                    callback_data="voucher_25"
                )
            ],


            [
                InlineKeyboardButton(
                    text="💵 ووچر 50 دلاری",
                    callback_data="voucher_50"
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


    return keyboard





# =========================
# پنل ادمین
# =========================


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
                    text="🎁 مدیریت ووچر",
                    callback_data="admin_vouchers"
                )
            ],


            [
                InlineKeyboardButton(
                    text="💳 سفارش‌ها",
                    callback_data="admin_orders"
                )
            ],


            [
                InlineKeyboardButton(
                    text="📢 پیام همگانی",
                    callback_data="admin_broadcast"
                )
            ],


            [
                InlineKeyboardButton(
                    text="⚙️ تنظیمات",
                    callback_data="admin_settings"
                )
            ]

        ]

    )


    return keyboard
