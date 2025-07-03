from flask import Flask, request
import requests
import os
import openai
from scaling import scaling_movements
from movement_times import movement_times
from weights_scaling import weights_scaling
from cardio_conversion import cardio_conversion, meters_equivalent

# CONFIG
BOT_TOKEN = '7952515157:AAGrKDHNW5USeWVV4WoR5C7u7BX9LVxkOgk'
BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

@app.route('/')
def home():
    return 'R2F Bot is live!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        lower_text = text.lower()
        reply = None

        if text == "/tool":
            reply = (
                "Scrivimi qui sotto la tua domanda sulla programmazione R2F.\n\n"
                "Puoi chiedere qualsiasi cosa su:\n"
                "• Scaling e alternative\n"
                "• Stimolo previsto e pacing\n"
                "• Tempi target e TxR\n"
                "• Significato di esercizi o sigle\n"
                "• Consigli tecnici e tool\n\n"
                "Ti risponderò direttamente io 
