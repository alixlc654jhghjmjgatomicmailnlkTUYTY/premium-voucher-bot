from aiogram.types import Message, CallbackQuery

from config import ADMIN_ID
import database
import buttons



def check_admin(user_id):

    return user_id == ADMIN_ID





async def open_admin(message: Message):

    if not check_admin(message.from_user.id):

        await message.answer(
            "⛔ دسترسی ندارید"
        )

        return


    await message.answer(
        """
👑 پنل مدیریت Premium Voucher

مدیریت کامل ربات از اینجا انجام می‌شود:
        """,
        reply_markup=buttons.admin_menu()
    )







async def admin_callbacks(call: CallbackQuery):


    data = call.data



    # آمار ربات

    if data == "admin_stats":


        users = database.users_count()

        vouchers = database.vouchers_count()



        await call.message.answer(
            f"""
📊 آمار ربات

👥 کاربران:
{users}

🎁 تعداد ووچر:
{vouchers}
"""
        )





    # کاربران

    elif data == "admin_users":


        users = database.users_count()


        await call.message.answer(
            f"""
👥 مدیریت کاربران

تعداد کاربران ثبت شده:
{users}
"""
        )






    # ووچرها

    elif data == "admin_vouchers":


        await call.message.answer(
            """
🎁 مدیریت ووچر

امکانات:
➕ ساخت ووچر
📋 لیست ووچرها
🗑 حذف ووچر
"""
        )






    # سفارش ها

    elif data == "admin_orders":


        await call.message.answer(
            """
💳 سفارش‌ها

لیست سفارش‌های کاربران اینجا نمایش داده می‌شود.
"""
        )






    # پیام همگانی

    elif data == "admin_broadcast":


        await call.message.answer(
            """
📢 ارسال پیام همگانی

پیام خود را ارسال کنید.
"""
        )






    # تنظیمات

    elif data == "admin_settings":


        await call.message.answer(
            """
⚙️ تنظیمات

تنظیمات ربات:
✅ فعال
"""
        )



    await call.answer()
