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
    update = Update.de_json(request.get_json(force=True), application.bot)
    print(">> RAW update:", update)
    await application.process_update(update)
    return 'ok', 200

# 👇 Выполняем сразу, без __main__
async def startup():
    await setup_webhook()
    await application.initialize()
    await application.start()

asyncio.run(startup())  # 👈 Запускается даже при gunicorn
