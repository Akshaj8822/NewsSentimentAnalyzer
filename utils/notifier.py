# utils/notifier.py

import smtplib
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Email Configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Telegram Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_email(subject, body):
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            message = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAIL_ADDRESS, TO_EMAIL, message)
            print("[EMAIL] Sent successfully!")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, data=payload)
        print("[TELEGRAM] Sent successfully!")
    except Exception as e:
        print(f"[TELEGRAM ERROR] {e}")
