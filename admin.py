from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from buttons import (
    admin_menu,
    services_menu
)

import database

from config import ADMIN_ID



# =====================
# حالت های افزودن سایت
# =====================

class AddService(StatesGroup):

    name = State()

    url = State()

    api_key = State()

    api_secret = State()





def is_admin(user_id):

    return user_id == ADMIN_ID





# =====================
# باز کردن پنل
# =====================

async def open_admin(message):

    if not is_admin(
        message.from_user.id
    ):
        return


    await message.answer(

        """
👑 پنل مدیریت Premium Voucher

انتخاب کنید:
        """,

        reply_markup=admin_menu()

    )





# =====================
# کال بک های ادمین
# =====================

async def admin_callback(
        call,
        state: FSMContext
):

    data = call.data



    # آمار

    if data == "admin_stats":


        await call.message.answer(

            f"""
📊 آمار ربات

👥 کاربران:
{database.users_count()}

📦 سفارشات:
{database.orders_count()}
"""
        )





    # سرویس ها

    elif data == "admin_services":


        services = database.get_services()


        await call.message.answer(

            """
🔗 مدیریت سایت های ووچر

سرویس فعال:
            """,

            reply_markup=services_menu(
                services
            )

        )





    # افزودن سایت

    elif data == "add_service":


        await state.set_state(
            AddService.name
        )


        await call.message.answer(

            """
🌐 اسم سایت را بفرست:

مثال:
Premium Voucher
            """

        )





    await call.answer()





# =====================
# گرفتن اطلاعات سایت
# =====================


async def add_service_name(
        message: types.Message,
        state: FSMContext
):

    await state.update_data(

        name=message.text

    )


    await state.set_state(
        AddService.url
    )


    await message.answer(

        """
🔗 آدرس API سایت را بفرست:
        """

    )





async def add_service_url(
        message: types.Message,
        state: FSMContext
):

    await state.update_data(

        url=message.text

    )


    await state.set_state(
        AddService.api_key
    )


    await message.answer(

        """
🔑 API KEY را بفرست:
        """

    )





async def add_service_key(
        message: types.Message,
        state: FSMContext
):

    await state.update_data(

        api_key=message.text

    )


    await state.set_state(

        AddService.api_secret

    )


    await message.answer(

        """
🔐 Secret Key را بفرست:
        """

    )





async def add_service_secret(
        message: types.Message,
        state: FSMContext
):

    data = await state.get_data()


    database.add_service(

        data["name"],

        data["url"],

        data["api_key"],

        message.text

    )


    await state.clear()


    await message.answer(

        """
✅ سایت ووچر با موفقیت اضافه شد

از این به بعد می‌توانی از این سرویس استفاده کنی.
        """

    )
