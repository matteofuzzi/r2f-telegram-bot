from flask import Flask, request
import requests
import os
import openai
from scaling import get_exercise_scaling
from weights import get_weight_scaling
from txr import calculate_virtual_time

app = Flask(__name__)

BOT_TOKEN = open("/etc/secrets/BOT_TOKEN").read().strip()
BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return 'R2F Bot is live!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text.startswith("/tool"):
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

        elif text.lower().startswith("/txr"):
            wod_text = text.replace("/txr", "").strip()
            reply = calculate_virtual_time(wod_text)

        elif any(keyword in text.lower() for keyword in ["scaling", "scale", "modifica", "regressione"]):
            exercise = text.split()[-1].upper()
            reply = get_exercise_scaling(exercise)

        elif "peso" in text.lower() or "weight" in text.lower():
            reply = get_weight_scaling(text)

        else:
            # fallback AI answer (CrossFit rules, coaching tips, stimoli ecc.)
            prompt = (
                f"Rispondi come se fossi il coach della programmazione R2F, "
                f"basandoti sullo storico CrossFit, le regole R2F su scaling, TxR, pacing e stimolo. "
                f"Domanda dell’utente: {text}"
            )
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Sei il coach della programmazione R2F. Rispondi con competenza tecnica e tono autorevole ma amichevole."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.6,
                    max_tokens=600
                )
                reply = completion.choices[0].message.content
            except Exception as e:
                reply = f"❌ Errore nella risposta AI: {str(e)}"

        requests.post(BOT_URL, json={
            'chat_id': chat_id,
            'text': reply
        })

    return '', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
