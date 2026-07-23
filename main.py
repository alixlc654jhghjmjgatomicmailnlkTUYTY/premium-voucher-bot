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

from payment_callback import check_and_complete



logging.basicConfig(
    level=logging.INFO
)


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
⚡ تحویل سریع

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
async def callback_handler(
        call: types.CallbackQuery
):

    data = call.data



    if data.startswith("admin_"):

        await admin_callback(call)

        return




    # خرید

    if data == "buy":

        await call.message.edit_text(
            """
🎁 انتخاب محصول:
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




    # ساخت پرداخت

    elif data.startswith("charge_"):


        amount = int(
            data.split("_")[1]
        )


        payment = create_payment(
            amount,
            call.from_user.id
        )


        if "error" in payment:

            await call.message.answer(
                "❌ خطا در ساخت پرداخت"
            )

            return



        database.add_transaction(

            call.from_user.id,

            amount,

            payment["authority"]

        )


        await call.message.answer(

            f"""
💳 فاکتور پرداخت

💰 مبلغ:
{amount:,} تومان

🆔 شناسه:
{payment['authority']}


برای تست تایید پرداخت:
 /verify {payment['authority']} {amount}
            """
        )





    # تست تایید پرداخت

    elif data == "verify":


        await call.message.answer(
            "از دستور /verify استفاده کنید."
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
📦 سفارشات شما خالی است.
"""
        )





    # پشتیبانی

    elif data == "support":

        await call.message.answer(
            """
🆘 پشتیبانی
"""
        )





    elif data.startswith("premium_"):


        await call.message.answer(
            """
⏳ در حال بررسی خرید...
"""
        )





    elif data == "back":

        await call.message.edit_text(

            "منوی اصلی 👇",

            reply_markup=main_menu()

        )



    await call.answer()






# ======================
# تایید پرداخت دستی
# ======================

@dp.message(Command("verify"))
async def verify(message: types.Message):


    try:

        args = message.text.split()


        authority = args[1]

        amount = int(args[2])


        result = check_and_complete(

            authority,

            message.from_user.id,

            amount

        )


        if result:

            await message.answer(
                """
✅ پرداخت تایید شد

💰 موجودی شما افزایش یافت.
"""
            )

        else:

            await message.answer(
                """
❌ پرداخت تایید نشد.
"""
            )


    except:


        await message.answer(
            """
فرمت صحیح:

/verify شناسه مبلغ
"""
        )





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
