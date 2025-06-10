from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Добро пожаловать! Введите свою дату и место рождения.")

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
