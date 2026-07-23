import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from dotenv import load_dotenv

from buttons import main_menu


load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        """
🤖 <b>Premium Voucher</b>

سلام 👋
به ربات ووچر خوش آمدید.

یکی از گزینه‌های زیر را انتخاب کنید:
        """,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )


@dp.message()
async def all_messages(message: Message):

    await message.answer(
        "از منوی زیر استفاده کنید 👇",
        reply_markup=main_menu()
    )


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
