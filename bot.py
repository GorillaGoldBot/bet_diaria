import time
import requests

TELEGRAM_TOKEN = "8821213951:AAFAovIS4NZoT9Eto8RZ4E-PKA6_0-2c_Gc"
CHAT_ID = "8679229910"


def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "Markdown"}
    requests.post(url, json=payload)


mensagem = (
    "🦍 *GORILLA GOLD BOT - ANÁLISE DIÁRIA*\n\n"
    "Olá, Lucas! Aqui está a seleção de hoje:\n\n"
    "🎯 *Entrada Principal:*\n"
    "• *Jogo:* Bayern de Munique vs Union Berlin\n"
    "• *Mercado:* Bayern Vence + Mais de 1.5 Gols\n"
    "• *Odd:* ~1.55"
)

while True:
    enviar_mensagem(mensagem)
    print("Mensagem enviada! Aguardando 24 horas...")
    time.sleep(86400)
