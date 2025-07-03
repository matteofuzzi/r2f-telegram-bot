from flask import Flask, request
import requests
import os
import openai
import re
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

def calculate_txr(text):
    pattern = r"(\d+)\s+([a-zA-Z\-+&/() ]+)"
    matches = re.findall(pattern, text)
    total_seconds = 0.0
    dettagli = []

    for qty, movement in matches:
        movement_clean = movement.strip().upper().replace("  ", " ")
        reps = int(qty)
        for key in movement_times:
            if key.upper() in movement_clean:
                seconds = reps * movement_times[key]
                total_seconds += seconds
                dettagli.append(f"{reps} {key} × {movement_times[key]}\" = {round(seconds)}\"")
                break

    minuti = int(total_seconds // 60)
    secondi = int(total_seconds % 60)
    time_str = f"{minuti}:{secondi:02d}"

    dettagli_txt = "\n".join(dettagli)
    return f"[TxR ESTIMATO]\n\n{dettagli_txt}\n\n→ Totale stimato: ~{time_str}"

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
