import requests
from django.conf import settings

token = settings.TELEGRAM_BOT_TOKEN
chat_id = settings.TELEGRAM_CHAT_IDS

def send_telegram_message(message):
  url = f"https://api.telegram.org/bot{token}/sendMessage"

  for chat_id in settings.TELEGRAM_CHAT_IDS:
      data = {
          "chat_id": chat_id,
          "text": message,
          "parse_mode": "HTML"
      }
      requests.post(url, data=data)
  
  try:
    response = requests.post(url, data=data)
    response.raise_for_status()
  except Exception as e:
    print("Telegram ERROR:", e)