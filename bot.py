from datetime import datetime
import requests

# --- CONFIGURAÇÕES ---
TELEGRAM_TOKEN = "8821213951:AAFAovIS4NZoT9Eto8RZ4E-PKA6_0-2c_Gc"
CHAT_ID = "8679229910"
API_FOOTBALL_KEY = "0e04466c8e49206b70eb3c5fc3ecb891"


def obter_jogos_hoje():
    hoje = datetime.now().strftime("%Y-%m-%d")
    url = f"https://v3.football.api-sports.io/fixtures?date={hoje}"
    headers = {
        "x-rapidapi-host": "v3.football.api-sports.io",
        "x-rapidapi-key": API_FOOTBALL_KEY,
    }

    try:
        resposta = requests.get(url, headers=headers)
        dados = resposta.json()
        jogos = dados.get("response", [])
        return jogos
    except Exception as e:
        print(f"Erro ao procurar jogos: {e}")
        return []


def enviar_mensagem_telegram(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto, "parse_mode": "Markdown"}
    requests.post(url, json=payload)


# --- EXECUÇÃO DO BOT ---
jogos = obter_jogos_hoje()

if jogos:
    mensagem = f"🦍 *GORILLA GOLD BOT - JOGOS DE HOJE ({len(jogos)} encontrados)*\n\n"
    for jogo in jogos[:5]:
        casa = jogo["teams"]["home"]["name"]
        fora = jogo["teams"]["away"]["name"]
        liga = jogo["league"]["name"]
        mensagem += f"• *{liga}:* {casa} vs {fora}\n"
else:
    mensagem = (
        "🦍 *GORILLA GOLD BOT ATIVADO!*\n\nSem jogos encontrados para hoje."
    )

enviar_mensagem_telegram(mensagem)
