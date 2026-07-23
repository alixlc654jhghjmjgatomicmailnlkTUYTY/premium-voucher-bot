import requests

from config import API_KEY, API_SECRET, API_URL



def get_voucher(product):

    try:

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }


        data = {

            "product": product,

            "secret": API_SECRET

        }


        response = requests.post(
            API_URL,
            json=data,
            headers=headers,
            timeout=20
        )


        result = response.json()



        if result.get("code"):

            return {

                "success": True,

                "code": result["code"]

            }



        return {

            "success": False,

            "error": "voucher_not_found"

        }



    except Exception as e:


        return {

            "success": False,

            "error": str(e)

        }
