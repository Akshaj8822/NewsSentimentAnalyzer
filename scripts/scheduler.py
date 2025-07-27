import schedule
import time
from scripts.fetch_news import fetch_news
from scripts.analyze_sentiment import analyze_sentiment

def job():
    print("🔄 Running scheduled task...")
    fetch_news()
    analyze_sentiment()
    print("✅ Task completed.\n")

def run_scheduler():
    schedule.every(60).minutes.do(job)  # Change to .minutes for faster testing

    print("🕒 Scheduler started. Press Ctrl+C to stop.\n")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
