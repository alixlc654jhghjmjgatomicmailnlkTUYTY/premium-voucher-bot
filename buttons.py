from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# =========================
# منوی اصلی کاربر
# =========================

def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎁 خرید ووچر",
                    callback_data="buy"
                ),
                InlineKeyboardButton(
                    text="💎 محصولات",
                    callback_data="products"
                )
            ],


            [
                InlineKeyboardButton(
                    text="💰 کیف پول",
                    callback_data="balance"
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
                    text="🎟 کد تخفیف",
                    callback_data="discount"
                )
            ],


            [
                InlineKeyboardButton(
                    text="⭐ دعوت دوستان",
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




# =========================
# انتخاب ووچر
# =========================

def voucher_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="💎 ووچر 10 دلاری",
                    callback_data="voucher_10"
                )
            ],


            [
                InlineKeyboardButton(
                    text="💎 ووچر 25 دلاری",
                    callback_data="voucher_25"
                )
            ],


            [
                InlineKeyboardButton(
                    text="💎 ووچر 50 دلاری",
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




# =========================
# پنل مدیریت
# =========================

def admin_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[


            [
                InlineKeyboardButton(
                    text="📊 آمار ربات",
                    callback_data="stats"
                ),

                InlineKeyboardButton(
                    text="👥 کاربران",
                    callback_data="users"
                )
            ],


            [
                InlineKeyboardButton(
                    text="🎁 مدیریت ووچر",
                    callback_data="vouchers"
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
                    callback_data="broadcast"
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
