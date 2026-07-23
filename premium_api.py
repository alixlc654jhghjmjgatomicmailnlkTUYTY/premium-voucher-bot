import requests
import hashlib
import time

from config import API_KEY, API_SECRET, API_URL



def signature(data):

    text = API_SECRET + str(data)

    return hashlib.sha256(
        text.encode()
    ).hexdigest()



def create_voucher(amount):


    data = {
        "amount": amount,
        "time": int(time.time())
    }


    headers = {

        "X-API-KEY": API_KEY,

        "X-SIGNATURE": signature(data)

    }



    try:

        response = requests.post(
            API_URL,
            json=data,
            headers=headers,
            timeout=30
        )


        return response.json()


    except Exception as e:


        return {
            "status":False,
            "error":str(e)
        }
