import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import BOT_TOKEN

import database

from buttons import (
    main_menu,
    products_menu,
    charge_menu
)

from admin import (
    open_admin,
    admin_callback
)


logging.basicConfig(level=logging.INFO)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()



# =====================
# START
# =====================

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
💰 کیف پول
⚡ تحویل سریع

یکی از گزینه‌ها را انتخاب کنید 👇
        """,
        reply_markup=main_menu()
    )



# =====================
# ADMIN
# =====================

@dp.message(Command("admin"))
async def admin_panel(message: types.Message):

    await open_admin(message)



# =====================
# BUTTONS
# =====================

@dp.callback_query()
async def callback_handler(call: types.CallbackQuery):

    data = call.data


    # پنل ادمین

    if data.startswith("admin_"):

        await admin_callback(call)

        return



    # خرید ووچر

    if data == "buy":

        await call.message.edit_text(
            """
🎁 انتخاب محصول:

یکی را انتخاب کنید 👇
            """,
            reply_markup=products_menu()
        )



    # شارژ حساب

    elif data == "charge":

        await call.message.answer(
            """
💳 مبلغ شارژ را انتخاب کنید:
            """,
            reply_markup=charge_menu()
        )



    # مبلغ شارژ

    elif data.startswith("charge_"):

        amount = int(
            data.split("_")[1]
        )

        await call.message.answer(
            f"""
💳 فاکتور شارژ

مبلغ:
{amount:,} تومان

⏳ درگاه پرداخت به زودی متصل می‌شود.
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

{balance} تومان
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



    # سفارشات

    elif data == "orders":

        await call.message.answer(
            """
📦 سفارش‌های شما

هنوز سفارشی ثبت نشده.
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
⏳ درخواست خرید ثبت شد.

در حال بررسی موجودی ووچر...
            """
        )



    # برگشت

    elif data == "back":

        await call.message.edit_text(
            "منوی اصلی 👇",
            reply_markup=main_menu()
        )



    await call.answer()



# =====================
# RUN
# =====================

async def main():

    database.init_db()

    print("🤖 Premium Voucher Started")

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
