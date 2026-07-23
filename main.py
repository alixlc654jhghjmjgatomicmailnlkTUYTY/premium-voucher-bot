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

from payment import create_payment

from premium_api import get_voucher



logging.basicConfig(level=logging.INFO)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()



# ======================
# START
# ======================

@dp.message(CommandStart())
async def start(message: types.Message):

    database.add_user(
        message.from_user.id,
        message.from_user.username
    )

    await message.answer(
        """
💎 خوش آمدید به Premium Voucher

🎁 خرید ووچر
💳 شارژ کیف پول
⚡ تحویل سریع و خودکار

انتخاب کنید 👇
        """,
        reply_markup=main_menu()
    )



# ======================
# ADMIN
# ======================

@dp.message(Command("admin"))
async def admin(message: types.Message):

    await open_admin(message)



# ======================
# CALLBACK
# ======================

@dp.callback_query()
async def callback_handler(call: types.CallbackQuery):

    data = call.data



    if data.startswith("admin_"):

        await admin_callback(call)
        return




    # خرید

    if data == "buy":

        await call.message.edit_text(
            """
🎁 محصول مورد نظر را انتخاب کنید:
            """,
            reply_markup=products_menu()
        )





    # شارژ

    elif data == "charge":

        await call.message.answer(
            """
💳 مبلغ شارژ را انتخاب کنید:
            """,
            reply_markup=charge_menu()
        )





    # خرید محصول

    elif data.startswith("premium_"):


        products = {

            "premium_1":
            ("تلگرام پریمیوم 1 ماهه", 100000),

            "premium_3":
            ("تلگرام پریمیوم 3 ماهه", 250000),

            "premium_6":
            ("تلگرام پریمیوم 6 ماهه", 450000)

        }


        product, price = products[data]


        balance = database.get_balance(
            call.from_user.id
        )



        if balance < price:


            await call.message.answer(
                """
❌ موجودی کافی نیست

ابتدا کیف پول خود را شارژ کنید.
"""
            )

            return





        await call.message.answer(
            "⏳ در حال دریافت ووچر..."
        )



        voucher = get_voucher(product)



        if not voucher.get("success"):


            await call.message.answer(
                """
❌ ووچر موجود نیست.
"""
            )

            return





        database.add_balance(
            call.from_user.id,
            -price
        )


        database.add_order(
            call.from_user.id,
            product,
            price
        )



        await call.message.answer(
            f"""
🎉 خرید موفق بود

💎 محصول:
{product}

🎁 کد ووچر:

`{voucher['code']}`

ممنون از خرید شما ❤️
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

{balance:,} تومان
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
📦 سفارشات شما
"""
        )





    # پشتیبانی

    elif data == "support":

        await call.message.answer(
            """
🆘 پشتیبانی
"""
        )





    # برگشت

    elif data == "back":

        await call.message.edit_text(
            "منوی اصلی 👇",
            reply_markup=main_menu()
        )



    await call.answer()





# ======================
# RUN
# ======================

async def main():

    database.init_db()

    print(
        "🤖 Premium Voucher Started"
    )

    await dp.start_polling(bot)




if __name__ == "__main__":

    asyncio.run(main())
