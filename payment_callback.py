from database import (
    add_balance,
    complete_transaction
)

from payment import verify_payment



def check_and_complete(
        authority,
        user_id,
        amount
):


    result = verify_payment(
        authority
    )



    if result.get("success"):


        # افزایش موجودی کاربر

        add_balance(
            user_id,
            amount
        )


        # تغییر وضعیت تراکنش

        complete_transaction(
            authority
        )


        return True



    return False
