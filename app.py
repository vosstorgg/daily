from flask import Flask, request
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
        application.update_queue.put_nowait(update)
        return 'ok', 200

if __name__ == '__main__':
    setup_webhook()
    app.run(host='0.0.0.0', port=8000)