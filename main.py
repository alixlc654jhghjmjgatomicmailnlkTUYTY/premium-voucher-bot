import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN

import database


from buttons import (
    main_menu
)


from admin import (
    open_admin,
    admin_callback,
    add_service_name,
    add_service_url,
    add_service_key,
    add_service_secret,
    AddService
)


from aiogram import F



logging.basicConfig(
    level=logging.INFO
)



bot = Bot(
    token=BOT_TOKEN
)


dp = Dispatcher(
    storage=MemoryStorage()
)





# =====================
# شروع
# =====================


@dp.message(CommandStart())
async def start(
        message: types.Message
):


    database.add_user(

        message.from_user.id,

        message.from_user.username

    )


    await message.answer(

        """
💎 Premium Voucher

🎁 خرید ووچر
💳 کیف پول
⚡ فروش خودکار

انتخاب کنید 👇
        """,

        reply_markup=main_menu()

    )





# =====================
# پنل ادمین
# =====================


@dp.message(Command("admin"))
async def admin_panel(
        message: types.Message
):

    await open_admin(
        message
    )





# =====================
# کال بک ها
# =====================


@dp.callback_query()
async def callbacks(

        call: types.CallbackQuery

):


    if call.data.startswith("admin") or call.data in [

        "add_service",
        "admin_services",
        "admin_stats"

    ]:


        await admin_callback(

            call,

            dp.fsm.get_context(
                bot,
                call.message.chat.id,
                call.from_user.id
            )

        )

        return



    await call.answer()





# =====================
# گرفتن اطلاعات سایت
# =====================


@dp.message(
    AddService.name
)
async def service_name(
        message: types.Message,
        state=None
):

    await add_service_name(

        message,

        state

    )





@dp.message(
    AddService.url
)
async def service_url(
        message: types.Message,
        state=None
):

    await add_service_url(

        message,

        state

    )





@dp.message(
    AddService.api_key
)
async def service_key(
        message: types.Message,
        state=None
):

    await add_service_key(

        message,

        state

    )





@dp.message(
    AddService.api_secret
)
async def service_secret(
        message: types.Message,
        state=None
):

    await add_service_secret(

        message,

        state

    )





# =====================
# اجرا
# =====================


async def main():

    database.init_db()


    print(
        "🤖 Bot Started"
    )


    await dp.start_polling(
        bot
    )





if __name__ == "__main__":

    asyncio.run(main())
