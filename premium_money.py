import httpx
from app.config import PREMIUM_API_KEY, PREMIUM_SECRET

class PremiumMoney:
    def __init__(self):
        self.client = httpx.AsyncClient(
            headers={
                "X-API-KEY": PREMIUM_API_KEY,
                "X-API-SECRET": PREMIUM_SECRET
            }
        )

    async def get_products(self):
        return {"status": "ready"}
