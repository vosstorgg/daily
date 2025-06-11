import asyncio
from telegram.ext import ApplicationBuilder
from handlers import register_handlers
from config import BOT_TOKEN
from db import init_db

async def main():
    await init_db()  # создаём таблицу, если ещё нет
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(app)
    await app.run_polling()  # запускаем бота

if __name__ == "__main__":
    asyncio.run(main())
