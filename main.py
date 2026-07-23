import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from config import BOT_TOKEN, ADMIN_ID

from database import (
    init_db,
    add_user,
    get_balance,
    add_balance,
    add_order,
    get_voucher,
    users_count,
    orders_count
)

from buttons import (
    main_menu,
    products_menu
)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()



# شروع ربات
@dp.message(Command("start"))
async def start(message: types.Message):

    add_user(
        message.from_user.id,
        message.from_user.username
    )

    text = """
🤖 خوش آمدید به Premium Voucher

🎁 فروش ووچرهای دیجیتال
⚡ تحویل سریع
🔒 امن و مطمئن

یکی از گزینه‌ها را انتخاب کنید:
"""

    await message.answer(
        text,
        reply_markup=main_menu()
    )



# پنل ادمین
@dp.message(Command("admin"))
async def admin(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return


    text=f"""
👑 پنل مدیریت

👥 کاربران:
{users_count()}

📦 سفارشات:
{orders_count()}
"""


    await message.answer(text)



# مدیریت دکمه ها
@dp.callback_query()
async def callbacks(call: CallbackQuery):


    data = call.data


    # خرید ووچر
    if data == "buy":

        await call.message.edit_text(
            "🎁 محصول مورد نظر را انتخاب کنید:",
            reply_markup=products_menu()
        )


    # موجودی
    elif data == "balance":

        bal = get_balance(
            call.from_user.id
        )

        await call.message.answer(
            f"""
💰 موجودی حساب شما:

{bal} تومان
"""
        )


    # پروفایل
    elif data == "profile":

        await call.message.answer(
            f"""
👤 حساب کاربری

🆔 آیدی:
{call.from_user.id}

💰 موجودی:
{get_balance(call.from_user.id)}
"""
        )


    # پشتیبانی
    elif data == "support":

        await call.message.answer(
            """
🆘 پشتیبانی

برای ارتباط با پشتیبانی پیام ارسال کنید.
"""
        )



    # محصولات


    elif data.startswith("premium_"):


        products = {

            "premium_1":
            ("تلگرام پریمیوم ۱ ماهه", 100000),

            "premium_3":
            ("تلگرام پریمیوم ۳ ماهه", 250000),

            "premium_6":
            ("تلگرام پریمیوم ۶ ماهه", 450000)

        }


        product,price = products[data]


        balance = get_balance(
            call.from_user.id
        )


        if balance < price:

            await call.message.answer(
                f"""
❌ موجودی کافی نیست

💰 قیمت:
{price}

موجودی شما:
{balance}
"""
            )

            return



        code = get_voucher(product)


        if not code:

            await call.message.answer(
                "❌ موجودی ووچر این محصول تمام شده"
            )

            return



        add_balance(
            call.from_user.id,
            -price
        )


        add_order(
            call.from_user.id,
            product,
            price
        )


        await call.message.answer(
            f"""
✅ خرید موفق بود 🎉

🎁 محصول:
{product}

🔑 کد ووچر:

`{code}`

ممنون از خرید شما 💎
"""
        )



    elif data == "back":

        await call.message.edit_text(
            "منوی اصلی:",
            reply_markup=main_menu()
        )



    await call.answer()



async def main():

    init_db()

    print("🤖 Premium Voucher Bot Started")

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())
