import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing")


bot = Bot(token=TOKEN)
dp = Dispatcher()


def main_menu():
    return InlineKeyboardMarkup(
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
                    text="📞 پشتیبانی",
                    callback_data="support"
                )
            ]
        ]
    )


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🤖 Premium Voucher\n\n"
        "به ربات خوش آمدید 👋\n"
        "از منوی زیر انتخاب کنید:",
        reply_markup=main_menu()
    )


@dp.callback_query()
async def buttons(callback: CallbackQuery):

    if callback.data == "get_voucher":
        await callback.message.answer(
            "🎁 بخش دریافت ووچر به زودی فعال می‌شود."
        )

    elif callback.data == "balance":
        await callback.message.answer(
            "💰 موجودی شما: 0 تومان"
        )

    elif callback.data == "support":
        await callback.message.answer(
            "📞 پشتیبانی:\n@YourUsername"
        )

    await callback.answer()


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
