from telegram.ext import ApplicationBuilder
from handlers import register_handlers
from config import BOT_TOKEN
from db import init_db
import asyncio

app = ApplicationBuilder().token(BOT_TOKEN).build()
register_handlers(app)

if __name__ == "__main__":
    asyncio.run(init_db())  # создаёт таблицу, если её ещё нет
    app.run_polling()
