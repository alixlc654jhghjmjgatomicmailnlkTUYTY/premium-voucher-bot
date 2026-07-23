import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import BOT_TOKEN, ADMIN_ID, SUPPORT

import database

from buttons import (
    main_menu,
    admin_menu,
    voucher_menu
)

from premium_api import create_voucher


logging.basicConfig(level=logging.INFO)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()



# =========================
# استارت
# =========================

@dp.message(CommandStart())
async def start(message: types.Message):

    database.add_user(
        message.from_user.id,
        message.from_user.username
    )


    await message.answer(
        """
💎 به Premium Voucher خوش آمدید

🎁 خرید ووچر پریمیوم
⚡ سریع و امن
💳 فروش خودکار

از منوی زیر انتخاب کنید 👇
        """,

        reply_markup=main_menu()
    )



# =========================
# پنل ادمین
# =========================

@dp.message(Command("admin"))
async def admin(message: types.Message):

    if message.from_user.id != ADMIN_ID:

        await message.answer(
            "⛔ دسترسی ندارید"
        )

        return


    await message.answer(
        """
👑 پنل مدیریت Premium Voucher
        """,

        reply_markup=admin_menu()
    )




# =========================
# مدیریت دکمه ها
# =========================

@dp.callback_query()
async def buttons_handler(
        call: types.CallbackQuery
):


    data = call.data



    # خرید

    if data == "buy":


        await call.message.answer(

            """
💎 مقدار ووچر را انتخاب کنید:
            """,

            reply_markup=voucher_menu()

        )





    # محصولات

    elif data == "products":


        await call.message.answer(

            """
💎 محصولات موجود:

🎁 ووچر 10 دلاری
🎁 ووچر 25 دلاری
🎁 ووچر 50 دلاری

یکی را انتخاب کنید.
            """,

            reply_markup=voucher_menu()

        )






    # خرید ووچرهای مختلف

    elif data.startswith("voucher_"):


        amount = data.split("_")[1]


        await call.message.answer(
            f"""
⏳ در حال خرید ووچر {amount} دلاری...

لطفاً صبر کنید 💎
            """
        )


        result = create_voucher(
            amount
        )


        if result.get("code"):


            await call.message.answer(
                f"""
🎉 خرید موفق

🎁 کد ووچر:

`{result['code']}`

ممنون از خرید شما ❤️
                """
            )


        else:


            await call.message.answer(
                """
❌ خطا در دریافت ووچر

با پشتیبانی تماس بگیرید.
                """
            )






    # موجودی

    elif data == "balance":


        balance = database.get_balance(
            call.from_user.id
        )


        await call.message.answer(

            f"""
💰 کیف پول شما:

{balance}
            """

        )






    # سفارش ها

    elif data == "orders":


        await call.message.answer(

            """
📦 سفارش‌های شما

در حال حاضر سفارشی ندارید.
            """

        )






    # پروفایل

    elif data == "profile":


        await call.message.answer(

            f"""
👤 حساب کاربری

🆔 ID:
{call.from_user.id}

⭐ Premium User
            """

        )






    # تخفیف

    elif data == "discount":


        await call.message.answer(

            """
🎟 کد تخفیف خود را ارسال کنید.
            """

        )






    # دعوت

    elif data == "invite":


        await call.message.answer(

            """
⭐ دعوت دوستان

لینک دعوت شما ساخته می‌شود.
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





    # بازگشت

    elif data == "back":


        await call.message.answer(

            "منوی اصلی 👇",

            reply_markup=main_menu()

        )



    await call.answer()






# =========================
# اجرا
# =========================

async def main():


    database.create_tables()


    print(
        "🤖 Premium Voucher Started"
    )


    await dp.start_polling(bot)




if __name__ == "__main__":

    asyncio.run(main())
