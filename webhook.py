import os
import telegram

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g., https://yourproject.up.railway.app/webhook

def setup_webhook():
    bot = telegram.Bot(BOT_TOKEN)
    bot.set_webhook(url=WEBHOOK_URL)