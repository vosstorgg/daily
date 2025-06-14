from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from gpt_client import ask_gpt  # not used yet

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(">> /start triggered")
    await update.message.reply_text("Hello, world!")

start_handler = CommandHandler("start", start)
