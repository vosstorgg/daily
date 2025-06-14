# webhook.py
import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

async def setup_webhook():
    bot = Bot(BOT_TOKEN)
    await bot.set_webhook(url=WEBHOOK_URL)
