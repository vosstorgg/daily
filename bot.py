from telegram.ext import ApplicationBuilder
from handlers import register_handlers
from config import BOT_TOKEN
import asyncio

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    register_handlers(app)
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
