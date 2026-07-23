import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv


# =========================
# تنظیمات
# =========================

load_dotenv()

# توکن ربات تلگرام را اینجا بگذار
BOT_TOKEN = "اینجا_توکن_ربات"

# آیدی ادمین
ADMIN_ID = 8369041514


bot = Bot(BOT_TOKEN)
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
                    callback_data="get_voucher"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💰 موجودی من",
                    callback_data="balance"
                ),

                InlineKeyboardButton(
                    text="🛒 خرید ووچر",
                    callback_data="buy"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📦 سفارش‌های من",
                    callback_data="orders"
                ),

                InlineKeyboardButton(
                    text="👤 حساب کاربری",
                    callback_data="profile"
                )
            ],

            [
                InlineKeyboardButton(
                    text="❓ سوالات متداول",
                    callback_data="faq"
                )
            ],

            [
                InlineKeyboardButton(
                    text="☎️ پشتیبانی",
                    callback_data="support"
                )
            ]

        ]
    )

    return keyboard



# =========================
# پنل ادمین
# =========================


def admin_menu():

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="👑 مدیریت کاربران",
                    callback_data="users"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📊 آمار ربات",
                    callback_data="stats"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎁 ارسال ووچر",
                    callback_data="send_voucher"
                )
            ],

            [
                InlineKeyboardButton(
                    text="⬅️ برگشت",
                    callback_data="back"
                )
            ]

        ]
    )

    return keyboard



# =========================
# استارت
# =========================


@dp.message(Command("start"))
async def start(message: types.Message):

    text = """

🤖 خوش آمدید به Premium Voucher

🎁 خرید و دریافت ووچر پریمیوم
⚡ سریع و امن
💎 سرویس ویژه کاربران

یکی از گزینه‌ها را انتخاب کنید 👇

"""

    await message.answer(
        text,
        reply_markup=main_menu()
    )



# =========================
# ادمین
# =========================


@dp.message(Command("admin"))
async def admin(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "👑 پنل مدیریت فعال شد",
        reply_markup=admin_menu()
    )



# =========================
# دکمه ها
# =========================


@dp.callback_query()
async def buttons(callback: types.CallbackQuery):

    data = callback.data


    if data == "get_voucher":

        await callback.message.answer(
            "🎁 درخواست ووچر ثبت شد\n\n⏳ در حال بررسی..."
        )


    elif data == "balance":

        await callback.message.answer(
            "💰 موجودی شما:\n\n0 تومان"
        )


    elif data == "buy":

        await callback.message.answer(
            "🛒 بخش خرید ووچر\n\nبه زودی فعال می‌شود"
        )


    elif data == "orders":

        await callback.message.answer(
            "📦 سفارش‌های شما خالی است"
        )


    elif data == "profile":

        await callback.message.answer(
            f"👤 پروفایل شما\n\nID: {callback.from_user.id}"
        )


    elif data == "support":

        await callback.message.answer(
            "☎️ پشتیبانی:\n@your_support"
        )


    elif data == "faq":

        await callback.message.answer(
            "❓ سوالات متداول\n\nبه زودی تکمیل می‌شود"
        )


    elif data == "back":

        await callback.message.answer(
            "منوی اصلی",
            reply_markup=main_menu()
        )


    await callback.answer()



# =========================
# اجرا
# =========================


async def main():

    print("🤖 Premium Voucher Started")

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
