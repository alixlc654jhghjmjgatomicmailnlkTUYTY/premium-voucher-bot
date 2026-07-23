import requests

# =========================
# تنظیمات API ووچر
# =========================

# آدرس API سایت ووچر
API_URL = "https://api.premiummoney.com"

# کلید API را اینجا بگذار
API_KEY = "5hnzarlmxklp5atafzld2jaec0z6lzhv2erogdrgkycw1bb1omdu4vgnzql3ofl4ا"


# =========================
# هدر درخواست
# =========================

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}



# =========================
# گرفتن موجودی حساب
# =========================

def get_balance():

    try:

        response = requests.get(
            f"{API_URL}/balance",
            headers=headers
        )

        data = response.json()

        return data


    except Exception as e:

        return {
            "error": str(e)
        }



# =========================
# ساخت ووچر
# =========================

def create_voucher(amount):

    try:

        payload = {

            "amount": amount

        }


        response = requests.post(
            f"{API_URL}/voucher/create",
            json=payload,
            headers=headers
        )


        return response.json()


    except Exception as e:

        return {

            "error": str(e)

        }



# =========================
# بررسی ووچر
# =========================

def check_voucher(code):

    try:

        response = requests.post(

            f"{API_URL}/voucher/check",

            json={
                "code": code
            },

            headers=headers

        )


        return response.json()


    except Exception as e:

        return {

            "error": str(e)

        }
