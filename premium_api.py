import requests
import hashlib
import time

from config import (
    API_KEY,
    API_SECRET,
    API_URL
)



def create_sign(data):

    raw = API_SECRET + str(data)

    return hashlib.sha256(
        raw.encode()
    ).hexdigest()





def buy_voucher(amount):

    payload = {

        "amount": amount,

        "currency": "USD",

        "timestamp": int(time.time())

    }



    headers = {

        "API-Key": API_KEY,

        "Signature": create_sign(payload),

        "Content-Type": "application/json"

    }



    try:

        response = requests.post(

            API_URL,

            json=payload,

            headers=headers,

            timeout=30

        )


        return response.json()



    except Exception as error:


        return {

            "success": False,

            "message": str(error)

        }
