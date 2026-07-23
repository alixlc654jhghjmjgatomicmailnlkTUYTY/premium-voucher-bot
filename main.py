import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import BOT_TOKEN

import database

from buttons import (
    main_menu,
    products_menu
)

from admin import (
    open_admin,
    admin_callback
)


logging.basicConfig(
    level=logging.INFO
)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()



# =========================
# شروع ربات
# =========================

@dp.message(CommandStart())
async def start(message: types.Message):

    database.add_user(
        message.from_user.id,
        message.from_user.username
    )


    await message.answer(
        """
💎 خوش آمدید به Premium Voucher

🎁 خرید ووچر دیجیتال
⚡ تحویل سریع
🔒 سیستم امن فروش

از منوی زیر انتخاب کنید 👇
        """,

        reply_markup=main_menu()
    )



# =========================
# پنل مدیریت
# =========================

@dp.message(Command("admin"))
async def admin_panel(message: types.Message):

    await open_admin(message)




# =========================
# دکمه ها
# =========================

@dp.callback_query()
async def buttons(call: types.CallbackQuery):


    data = call.data



    # دکمه های ادمین

    if data.startswith("admin_"):

        await admin_callback(call)

        return




    # خرید

    if data == "buy":

        await call.message.edit_text(
            """
🎁 انتخاب محصول:

یکی از گزینه‌ها را انتخاب کنید:
            """,

            reply_markup=products_menu()
        )




    # موجودی

    elif data == "balance":


        balance = database.get_balance(
            call.from_user.id
        )


        await call.message.answer(

            f"""
💰 موجودی شما:

{balance} تومان
"""
        )




    # سفارش‌ها

    elif data == "orders":


        await call.message.answer(

            """
📦 سفارش‌های شما

در حال حاضر سفارشی ثبت نشده.
"""
        )





    # پروفایل

    elif data == "profile":


        await call.message.answer(

            f"""
👤 حساب کاربری

🆔 ID:
{call.from_user.id}
"""
        )





    # پشتیبانی

    elif data == "support":


        await call.message.answer(

            """
🆘 پشتیبانی

با پشتیبانی در ارتباط باشید.
"""
        )





    # محصولات

    elif data.startswith("premium_"):


        await call.message.answer(

            """
⏳ درخواست خرید ثبت شد

در حال بررسی موجودی ووچر...
"""
        )


        # اینجا بعداً API واقعی وصل می‌شود





    # بازگشت

    elif data == "back":


        await call.message.edit_text(

            "منوی اصلی 👇",

            reply_markup=main_menu()

        )


    await call.answer()




# =========================
# اجرا
# =========================

async def main():


    database.init_db()


    print(
        "🤖 Premium Voucher Started"
    )


    await dp.start_polling(bot)




if __name__ == "__main__":

    asyncio.run(main())
