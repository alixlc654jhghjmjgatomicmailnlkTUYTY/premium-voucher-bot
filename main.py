import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from aiogram.filters import Command


TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 8369041514


bot = Bot(token=TOKEN)
dp = Dispatcher()


def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎁 دریافت ووچر",
                    callback_data="voucher"
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
                )
            ]
        ]
    )


def admin_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👥 کاربران",
                    callback_data="users"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🎟 مدیریت ووچر",
                    callback_data="manage_voucher"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚙ تنظیمات",
                    callback_data="settings"
                )
            ]
        ]
    )


@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "🤖 به ربات Premium Voucher خوش آمدید\n\n"
        "یکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=main_menu()
    )


@dp.message(Command("admin"))
async def admin(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "👑 پنل مدیریت",
        reply_markup=admin_menu()
    )


@dp.callback_query()
async def callback(call: CallbackQuery):

    if call.data == "voucher":
        await call.message.answer(
            "🎁 بخش دریافت ووچر فعال شد"
        )

    elif call.data == "balance":
        await call.message.answer(
            "💰 موجودی شما: 0"
        )

    elif call.data == "buy":
        await call.message.answer(
            "🛒 بخش خرید ووچر"
        )

    elif call.data == "orders":
        await call.message.answer(
            "📦 سفارش‌های شما"
        )

    elif call.data == "users":
        await call.message.answer(
            "👥 مدیریت کاربران"
        )

    elif call.data == "manage_voucher":
        await call.message.answer(
            "🎟 مدیریت ووچر"
        )

    elif call.data == "settings":
        await call.message.answer(
            "⚙ تنظیمات"
        )

    await call.answer()


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
