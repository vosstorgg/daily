from telegram.ext import ApplicationBuilder
from handlers import register_handlers
from config import BOT_TOKEN

app = ApplicationBuilder().token(BOT_TOKEN).build()
register_handlers(app)

if __name__ == "__main__":
    app.run_polling()
