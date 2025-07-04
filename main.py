# main.py

import os
import requests
from flask import Flask, request
from scaling import get_scaling_for_movement

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").strip()

        reply = None
        if text:
            scaling = get_scaling_for_movement(text)
            if scaling:
                reply = scaling
            else:
                reply = "❌ Nessuno scaling trovato per questo movimento."

        if reply:
            requests.post(
                BOT_URL + "/sendMessage",
                json={"chat_id": chat_id, "text": reply}
            )

    return "", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
