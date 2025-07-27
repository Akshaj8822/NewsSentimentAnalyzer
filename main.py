from scripts.fetch_news import fetch_news
from scripts.analyze_sentiment import analyze_sentiment

def main():
    print("📥 Fetching latest news...")
    fetch_news()

    print("💬 Analyzing sentiment...")
    analyze_sentiment()

    print("✅ Done. Check data/headlines.csv for output.")

if __name__ == "__main__":
    main()
 
