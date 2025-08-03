import json
import time
import requests
import schedule

# Load config
with open("config.json") as f:
    config = json.load(f)

BITFINEX_API_KEY = config["bitfinex_api_key"]
BITFINEX_API_SECRET = config["bitfinex_api_secret"]
TELEGRAM_TOKEN = config["telegram_token"]
TELEGRAM_CHAT_ID = config["telegram_chat_id"]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    print("⏳ Trying to send message to Telegram...")
    print(f"URL: {url}")
    print(f"Payload: {payload}")

    try:
        response = requests.post(url, json=payload)
        print("✅ Response:", response.status_code, response.text)
    except Exception as e:
        print("❌ Telegram error:", e)
def check_market():
    try:
        response = requests.get("https://api-pub.bitfinex.com/v2/ticker/tETHUSD")
        data = response.json()
        price = data[6]
        send_telegram(f"ETH price is ${price}")
        # Example signal
        if price < 3700:
            send_telegram("🟥 ETH dropped below $3700! Consider SHORT (if confirmed).")
        elif price > 3880:
            send_telegram("🟩 ETH broke above $3880! Consider LONG (if confirmed).")
    except Exception as e:
        send_telegram(f"Market check error: {e}")

schedule.every(30).seconds.do(check_market)

send_telegram("🤖 Super Machine started and monitoring ETH/USDT...")

while True:
    schedule.run_pending()
    time.sleep(1)
def send_test():
    send_telegram("✅ Telegram test message from Super Machine.")

send_test()