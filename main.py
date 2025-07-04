from flask import Flask, request
import requests
import os
from scaling import get_scaling

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/')
def home():
    return 'R2F Bot is live!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '').strip()

        reply = get_scaling(text)

        requests.post(BOT_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
