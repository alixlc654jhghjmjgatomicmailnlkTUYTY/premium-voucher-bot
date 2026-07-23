import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import BOT_TOKEN, ADMIN_ID, SUPPORT

import database
from buttons import main_menu, admin_menu
from premium_api import create_voucher


logging.basicConfig(level=logging.INFO)


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

🎁 خرید ووچر پریمیوم
⚡ سریع و امن
💳 فروش خودکار

از منوی زیر انتخاب کنید 👇
        """,

        reply_markup=main_menu()
    )



# =========================
# پنل مدیریت
# =========================

@dp.message(Command("admin"))
async def admin_panel(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return


    await message.answer(
        """
👑 پنل مدیریت Premium Voucher

مدیریت ربات:
        """,

        reply_markup=admin_menu()
    )




# =========================
# دکمه ها
# =========================

@dp.callback_query()
async def callback_handler(call: types.CallbackQuery):

    data = call.data



    # خرید ووچر

    if data == "buy":


        await call.message.answer(
            """
💎 انتخاب مقدار ووچر:

10$
25$
50$

به زودی فعال می‌شود.
            """
        )




    # دریافت ووچر از API

    elif data == "get_voucher":


        await call.message.answer(
            "⏳ در حال اتصال به سیستم ووچر..."
        )


        result = create_voucher(10)


        if "code" in result:

            await call.message.answer(
                f"""
🎉 ووچر شما آماده شد:

🎁 {result['code']}
                """
            )

        else:

            await call.message.answer(
                """
❌ خطا در دریافت ووچر

بعداً دوباره تلاش کنید.
                """
            )




    # موجودی

    elif data == "balance":

        balance = database.get_balance(
            call.from_user.id
        )


        await call.message.answer(
            f"""
💰 موجودی شما:

{balance}
"""
        )




    # پروفایل

    elif data == "profile":


        await call.message.answer(
            f"""
👤 حساب کاربری

🆔 آیدی:
{call.from_user.id}

💎 Premium User
"""
        )




    # سفارش ها

    elif data == "orders":

        await call.message.answer(
            """
📦 سفارش‌های شما

هنوز سفارشی ندارید.
"""
        )




    # پشتیبانی

    elif data == "support":

        await call.message.answer(
            f"""
☎️ پشتیبانی:

{SUPPORT}
"""
        )




    # سوالات

    elif data == "faq":

        await call.message.answer(
            """
❓ سوالات متداول

1- زمان دریافت ووچر؟
2- روش پرداخت؟
3- پشتیبانی؟
"""
        )



    await call.answer()




# =========================
# اجرا
# =========================

async def main():

    database.create_tables()

    print("Premium Voucher Started")

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
