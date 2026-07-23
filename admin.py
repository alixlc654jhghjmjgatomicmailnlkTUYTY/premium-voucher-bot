from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID

from database import (
    users_count,
    orders_count
)



def is_admin(user_id):

    return user_id == ADMIN_ID




def admin_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="📊 آمار ربات",
                    callback_data="admin_stats"
                )
            ],

            [
                InlineKeyboardButton(
                    text="🎁 مدیریت ووچر",
                    callback_data="admin_voucher"
                )
            ],

            [
                InlineKeyboardButton(
                    text="👥 کاربران",
                    callback_data="admin_users"
                )
            ],

            [
                InlineKeyboardButton(
                    text="💰 مدیریت مالی",
                    callback_data="admin_money"
                )
            ]

        ]
    )





async def open_admin(message: types.Message):

    if not is_admin(
        message.from_user.id
    ):

        return


    await message.answer(
        """
👑 پنل مدیریت Premium Voucher

از منو انتخاب کنید:
""",

        reply_markup=admin_menu()
    )





async def admin_callback(call):


    data = call.data


    if data == "admin_stats":


        await call.message.answer(

            f"""
📊 آمار ربات

👥 کاربران:
{users_count()}

📦 سفارش‌ها:
{orders_count()}
"""
        )



    elif data == "admin_voucher":


        await call.message.answer(

            """
🎁 مدیریت ووچر

➕ افزودن ووچر
📋 لیست ووچرها
🗑 حذف ووچر
"""
        )



    elif data == "admin_users":


        await call.message.answer(

            """
👥 مدیریت کاربران

جستجو و مدیریت کاربران
"""
        )



    elif data == "admin_money":


        await call.message.answer(

            """
💰 مدیریت مالی

افزایش موجودی
بررسی پرداخت‌ها
"""
        )


    await call.answer()
