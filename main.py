import os
from telegram import Bot
from telegram.ext import Updater

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_alert(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def main():
    send_alert("🟢 Whale Hunter Bot started on Railway!")

if __name__ == "__main__":
    main()