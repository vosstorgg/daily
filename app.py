from flask import Flask, request
import asyncio
from telegram import Update
from webhook import setup_webhook
from bot import application

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

@app.route('/webhook', methods=['POST'])
async def webhook():
    try:
        update = Update.de_json(request.get_json(force=True), application.bot)
        print(">> RAW update:", update)
        asyncio.create_task(application.process_update(update))  # фоновая обработка
    except Exception as e:
        print(">> ERROR in webhook:", e)
    return 'ok', 200  # мгновенный ответ Telegram

async def startup():
    await setup_webhook()
    await application.initialize()
    await application.start()

asyncio.run(startup())