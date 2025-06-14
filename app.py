from flask import Flask, request
import asyncio
from webhook import setup_webhook
from bot import application

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = request.get_json(force=True)
        print(">> RAW update:", update)  # 👈 логируем весь апдейт
        application.update_queue.put_nowait(update)
        return 'ok', 200

if __name__ == '__main__':
    asyncio.run(setup_webhook())
