from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7952515157:AAGrKDHNW5USeWVV4WoR5C7u7BX9LVxkOgk'
BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/')
def home():
    return 'R2F Bot is live!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == "/tool":
            reply = (
                "Scrivimi qui sotto la tua domanda sulla programmazione R2F.\n\n"
                "Puoi chiedere qualsiasi cosa su:\n"
                "• Scaling e alternative\n"
                "• Stimolo previsto e pacing\n"
                "• Tempi target e TxR\n"
                "• Significato di esercizi o sigle\n"
                "• Consigli tecnici e tool\n\n"
                "Ti risponderò direttamente io 🤖"
            )
        else:
            reply = (
                "Ricevuto!\n\n"
                "Hai chiesto:\n"
                f"❓ {text}\n\n"
                "➡️ Il tuo messaggio è stato inoltrato al coach. Ti risponderò a breve!"
            )

        requests.post(BOT_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
