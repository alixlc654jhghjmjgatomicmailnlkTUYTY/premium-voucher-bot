import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_TOKEN, ADMIN_ID, WELCOME_TEXT


logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# =========================
# منوی اصلی
# =========================

def main_menu():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎁 دریافت ووچر",
                    callback_data="buy_voucher"
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



# =========================
# شروع ربات
# =========================

@dp.message(Command("start"))
async def start(message: types.Message):

    await message.answer(
        WELCOME_TEXT,
        reply_markup=main_menu()
    )



# =========================
# پنل ادمین
# =========================

@dp.message(Command("admin"))
async def admin(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👑 مدیریت",
                    callback_data="admin_panel"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📊 آمار کاربران",
                    callback_data="users_stats"
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
        "👑 پنل مدیریت Premium Voucher",
        reply_markup=keyboard
    )



# =========================
# دکمه ها
# =========================

@dp.callback_query()
async def buttons(callback: types.CallbackQuery):

    data = callback.data


    if data == "buy_voucher":

        await callback.message.answer(
            "🎁 بخش خرید ووچر\n\n"
            "در حال اتصال به سیستم فروش..."
        )


    elif data == "balance":

        await callback.message.answer(
            "💰 موجودی شما:\n"
            "در حال بررسی..."
        )


    elif data == "support":

        await callback.message.answer(
            "👤 پشتیبانی:\n"
            "@آیدی_پشتیبانی"
        )


    elif data == "admin_panel":

        await callback.message.answer(
            "👑 پنل مدیریت فعال شد"
        )


    elif data == "users_stats":

        await callback.message.answer(
            "📊 تعداد کاربران: در حال دریافت..."
        )


    elif data == "send_voucher":

        await callback.message.answer(
            "🎁 ارسال ووچر فعال شد"
        )


    await callback.answer()



# =========================
# اجرا
# =========================

async def main():

    print("🤖 Premium Voucher Bot Started")

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
