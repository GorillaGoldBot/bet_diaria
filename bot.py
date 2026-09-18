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
    return "Bot de Sinais Online"


# Lista de palpites do dia (pode adicionar quantos quiser)
SINAIS = [
    {
        "jogo": "Bayern de Munique vs Union Berlin",
        "liga": "Bundesliga",
        "mercado": "Bayern Vence + Mais de 1.5 Gols",
        "odd": "1.55",
        "horario": "15:30",
    },
    {
        "jogo": "Real Madrid vs Espanyol",
        "liga": "La Liga",
        "mercado": "Mais de 2.5 Gols",
        "odd": "1.60",
        "horario": "16:00",
    },
    {
        "jogo": "Manchester City vs Arsenal",
        "liga": "Premier League",
        "mercado": "Ambas Marcam (Sim)",
        "odd": "1.72",
        "horario": "18:00",
    },
]


def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Erro ao enviar: {e}")


def loop_bot():
    # 1. Envia um resumo inicial de todas as entradas do dia
    resumo = "🦍 *GORILLA GOLD BOT - LISTA DE SINAIS DO DIA*\n\n"
    for s in SINAIS:
        resumo += f"⚽ *{s['jogo']}* ({s['horario']})\n"
        resumo += f"🏆 {s['liga']} | 🎯 {s['mercado']} | 📈 Odd: {s['odd']}\n\n"

    enviar_mensagem(resumo)

    # 2. Envia alertas individuais com intervalo entre eles (ex: a cada 2 horas)
    intervalo_segundos = 7200  # 2 horas entre cada sinal individual

    while True:
        for sinal in SINAIS:
            alerta = (
                f"🚨 *SINAL CONFIRMADO - GORILLA GOLD*\n\n"
                f"📌 *Jogo:* {sinal['jogo']}\n"
                f"🏆 *Liga:* {sinal['liga']}\n"
                f"⏰ *Horário:* {sinal['horario']}\n\n"
                f"🎯 *Entrada:* {sinal['mercado']}\n"
                f"📈 *Odd Sugerida:* {sinal['odd']}\n\n"
                f"⚠️ _Gerencie sua banca com responsabilidade._"
            )
            enviar_mensagem(alerta)
            time.sleep(intervalo_segundos)


if __name__ == "__main__":
    threading.Thread(target=loop_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

