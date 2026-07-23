import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from config import BOT_TOKEN, ADMIN_ID, SUPPORT

import database
import buttons
import admin


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()



# ======================
# شروع ربات
# ======================

@dp.message(CommandStart())
async def start(message: Message):

    database.add_user(
        message.from_user.id,
        message.from_user.username
    )


    await message.answer(
        """
💎 به Premium Voucher خوش آمدید

🎁 خرید ووچر
💰 مدیریت کیف پول
📦 مشاهده سفارش‌ها

همه خدمات از منوی زیر:
        """,

        reply_markup=buttons.main_menu()
    )




# ======================
# پنل ادمین
# ======================

@dp.message(Command("admin"))
async def admin_panel(message: Message):

    await admin.open_admin(message)





# ======================
# دکمه‌ها
# ======================

@dp.callback_query()
async def all_buttons(call: CallbackQuery):


    data = call.data



    # پنل ادمین

    if data.startswith("admin_"):

        await admin.admin_callbacks(call)

        return




    # خرید ووچر

    if data == "buy_voucher":


        await call.message.answer(

            """
💎 انتخاب محصول

لطفاً مقدار ووچر را انتخاب کنید:
            """,

            reply_markup=buttons.products_menu()

        )





    # کیف پول

    elif data == "wallet":


        balance = database.get_balance(
            call.from_user.id
        )


        await call.message.answer(

            f"""
💰 کیف پول شما

موجودی:
{balance}
            """

        )





    # سفارش‌ها

    elif data == "orders":


        await call.message.answer(

            """
📦 سفارش‌های شما

فعلاً سفارشی ثبت نشده است.
            """

        )





    # تخفیف

    elif data == "discount":


        await call.message.answer(

            """
🎁 کد تخفیف

اگر کد دارید ارسال کنید.
            """

        )





    # دعوت

    elif data == "invite":


        await call.message.answer(

            """
👥 دعوت دوستان

لینک دعوت شما ساخته می‌شود.
            """

        )





    # پشتیبانی

    elif data == "support":


        await call.message.answer(

            f"""
☎️ پشتیبانی

{SUPPORT}
            """

        )




    # محصولات

    elif data.startswith("voucher_"):


        amount = data.split("_")[1]


        await call.message.answer(

            f"""
💎 درخواست ووچر {amount} دلاری ثبت شد.

در حال بررسی خرید...
            """

        )



    await call.answer()





# ======================
# اجرا
# ======================

async def main():

    database.create_tables()

    print("Premium Voucher Bot Started")

    await dp.start_polling(bot)




if __name__ == "__main__":

    asyncio.run(main())
