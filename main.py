import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message()
async def hello(message: Message):
    await message.answer("🤖 Premium Voucher فعال شد")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
