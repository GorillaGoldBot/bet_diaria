import os
import threading
import time
from flask import Flask
import requests

TELEGRAM_TOKEN = "8821213951:AAFAovIS4NZoT9Eto8RZ4E-PKA6_0-2c_Gc"
CHAT_ID = "8679229910"

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot Online"


def loop_bot():
    mensagem = (
        "🦍 *GORILLA GOLD BOT - ANÁLISE DIÁRIA*\n\n"
        "Olá, Lucas! Aqui está a seleção de hoje:\n\n"
        "🎯 *Entrada Principal:*\n"
        "• *Jogo:* Bayern de Munique vs Union Berlin\n"
        "• *Mercado:* Bayern Vence + Mais de 1.5 Gols\n"
        "• *Odd:* ~1.55"
    )
    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = {
                "chat_id": CHAT_ID,
                "text": mensagem,
                "parse_mode": "Markdown",
            }
            requests.post(url, json=payload)
            print("Mensagem enviada com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar: {e}")
        time.sleep(86400)


if __name__ == "__main__":
    threading.Thread(target=loop_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
