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


# ======================
# USER MENU
# ======================

def user_menu():

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
                    text="🛒 خرید",
                    callback_data="buy"
                )
            ],

            [
                InlineKeyboardButton(
                    text="📦 سفارش‌های من",
                    callback_data="orders"
               
