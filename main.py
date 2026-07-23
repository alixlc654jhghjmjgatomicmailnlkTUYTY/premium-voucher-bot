import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is missing")


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "🤖 Premium Voucher فعال شد!\n\n"
        "سلام 👋\n"
        "ربات با موفقیت روشن است."
    )


@dp.message()
async def all_messages(message: Message):
    await message.answer("✅ پیام دریافت شد")


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
