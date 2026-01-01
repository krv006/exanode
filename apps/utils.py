import requests

from apps.models import TelegramBot


def send_telegram_message(text: str):
    config = TelegramBot.objects.first()
    if not config:
        return False

    url = f"https://api.telegram.org/bot{config.telegram_token}/sendMessage"

    chats = [
        config.group_chat_id,
        config.admin_chat_id,
    ]

    for chat_id in chats:
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        try:
            requests.post(url, json=payload, timeout=10)
        except Exception:
            pass

    return True
