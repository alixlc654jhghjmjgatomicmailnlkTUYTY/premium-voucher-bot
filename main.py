import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise Exception("BOT_TOKEN تنظیم نشده")


bot = Bot(token=TOKEN)
dp = Dispatcher()


# منوی اصلی شیشه ای
def main_menu():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎁 دریافت ووچر",
                    callback_data="get_voucher"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💰 موجودی من",
                    callback_data="balance"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👤 پشتیبانی",
                    callback_data="support"
                )
            ]
        ]
    )

    return keyboard



# شروع ربات
@dp.message(Command("start"))
async def start(message: types.Message):

    await message.answer(
        "🤖 به Premium Voucher خوش آمدید\n\n"
        "از منوی زیر انتخاب کنید:",
        reply_markup=main_menu()
    )



# دکمه دریافت ووچر
@dp.callback_query(lambda c: c.data == "get_voucher")
async def get_voucher(call: types.CallbackQuery):

    await call.message.answer(
        "🎁 درخواست ووچر ثبت شد.\n"
        "لطفا منتظر تایید باشید."
    )



# موجودی
@dp.callback_query(lambda c: c.data == "balance")
async def balance(call: types.CallbackQuery):

    await call.message.answer(
        "💰 موجودی شما:\n0 تومان"
    )



# پشتیبانی
@dp.callback_query(lambda c: c.data == "support")
async def support(call: types.CallbackQuery):

    await call.message.answer(
        "☎️ ارتباط با پشتیبانی:\n@YourSupport"
    )



# پنل ادمین
ADMIN_ID = 8369041514


@dp.message(Command("admin"))
async def admin(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📊 آمار کاربران",
                    callback_data="users"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎁 ارسال ووچر",
                    callback_data="send_voucher"
                )
            ]
        ]
    )


    await message.answer(
        "👑 پنل مدیریت",
        reply_markup=keyboard
    )



async def main():

    print("Bot Started")

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
