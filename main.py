from flask import Flask, request
import requests
import os
import openai

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
            prompt = (
                f"Rispondi come se fossi il coach della programmazione R2F, "
                f"basandoti sullo storico CrossFit, le regole R2F su scaling, TxR, pacing e stimolo. "
                f"Domanda dell’utente: {text}"
            )

            try:
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Sei il coach della programmazione R2F. Rispondi con competenza tecnica e tono autorevole ma amichevole."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.6,
                    max_tokens=500
                )
                reply = response.choices[0].message.content

            except Exception as e:
                reply = f"❌ Errore nella risposta AI: {str(e)}"

        # Invia la risposta su Telegram
        requests.post(BOT_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)