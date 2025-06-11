import asyncio
from telegram.ext import ApplicationBuilder
from handlers import register_handlers
from config import BOT_TOKEN
from db import init_db

async def run():
    await init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(app)
    await app.initialize()
    await app.start()
    print("🤖 Бот запущен и работает")
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run())
    loop.run_forever()
