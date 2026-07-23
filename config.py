import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8369041514"))
CURRENCY = os.getenv("CURRENCY", "USD")
PREMIUM_API_KEY = os.getenv("PREMIUM_API_KEY")
PREMIUM_SECRET = os.getenv("PREMIUM_SECRET")
