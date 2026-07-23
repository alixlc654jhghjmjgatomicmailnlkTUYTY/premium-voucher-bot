from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# ======================
# منوی اصلی
# ======================

def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="🎁 خرید ووچر",
                    callback_data="buy"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💰 موجودی من",
                    callback_data="balance"
                ),

                InlineKeyboardButton(
                    text="👤 حساب کاربری",
                    callback_data="profile"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📦 سفارشات من",
                    callback_data="orders"
                ),

                InlineKeyboardButton(
                    text="🆘 پشتیبانی",
                    callback_data="support"
                )
            ]

        ]
    )





# ======================
# پنل ادمین
# ======================

def admin_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[


            [
                InlineKeyboardButton(
                    text="📊 آمار کاربران",
                    callback_data="admin_stats"
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
                    text="🔗 اتصال سایت ووچر",
                    callback_data="admin_services"
                )
            ],


            [
                InlineKeyboardButton(
                    text="⚙️ تنظیمات",
                    callback_data="admin_settings"
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





# ======================
# لیست سرویس ها
# ======================

def services_menu(services):


    buttons=[]


    for service in services:

        buttons.append([

            InlineKeyboardButton(

                text=f"🌐 {service[1]}",

                callback_data=f"service_{service[0]}"

            )

        ])



    buttons.append([

        InlineKeyboardButton(

            text="➕ افزودن سایت جدید",

            callback_data="add_service"

        )

    ])



    buttons.append([

        InlineKeyboardButton(

            text="⬅️ برگشت",

            callback_data="admin"

        )

    ])


    return InlineKeyboardMarkup(
        inline_keyboard=buttons
    )





# ======================
# محصولات
# ======================

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
                    text="💎 پریمیوم 3 ماهه",
                    callback_data="premium_3"
                )
            ],


            [
                InlineKeyboardButton(
                    text="👑 پریمیوم 6 ماهه",
                    callback_data="premium_6"
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





# ======================
# شارژ کیف پول
# ======================

def charge_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="💳 100 هزار تومان",
                    callback_data="charge_100"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💳 500 هزار تومان",
                    callback_data="charge_500"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💳 1 میلیون تومان",
                    callback_data="charge_1000"
                )
            ]

        ]
    )
