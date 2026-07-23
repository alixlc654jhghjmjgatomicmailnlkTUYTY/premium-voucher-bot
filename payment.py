import uuid
from datetime import datetime


# =========================
# تنظیمات درگاه پرداخت
# =========================

# کلید درگاه را اینجا قرار بده
PAYMENT_API_KEY = "اینجا_کلید_درگاه"


# آدرس برگشت
CALLBACK_URL = "https://example.com/payment/callback"



# =========================
# ساخت پرداخت
# =========================

def create_payment(amount, user_id):

    try:

        # این قسمت بعداً با API درگاه وصل می‌شود

        authority = str(uuid.uuid4())


        payment = {

            "authority": authority,

            "amount": amount,

            "user_id": user_id,

            "date":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )

        }


        return payment


    except Exception as e:

        return {
            "error": str(e)
        }



# =========================
# تایید پرداخت
# =========================

def verify_payment(authority):

    # بعداً درخواست واقعی API

    return True
