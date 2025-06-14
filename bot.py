import os
from telegram.ext import ApplicationBuilder
from handlers.start import start_handler

BOT_TOKEN = os.getenv("BOT_TOKEN")

application = ApplicationBuilder().token(BOT_TOKEN).build()

# Register handlers
application.add_handler(start_handler)