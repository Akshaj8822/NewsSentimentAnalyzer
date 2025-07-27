import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from utils.logger import get_logger

logger = get_logger(__name__)

def analyze_sentiment():
    try:
        # Load headlines data
        df = pd.read_csv("data/headlines.csv")

        # Initialize sentiment analyzer
        analyzer = SentimentIntensityAnalyzer()

        # Analyze sentiment for each row
        sentiments = []
        for _, row in df.iterrows():
            text = f"{row['title']} {row['description']}"
            score = analyzer.polarity_scores(text)
            sentiments.append(score['compound'])

        # Add sentiment scores to DataFrame
        df['sentiment'] = sentiments
        df.to_csv("data/headlines.csv", index=False)
        logger.info("✅ Sentiment analysis completed and saved.")

        # Calculate average sentiment
        avg_sentiment = df['sentiment'].mean()
        print(f"📢 Average Sentiment Score: {avg_sentiment:.3f}")

        # Alerts
        if avg_sentiment > 0.5:
            print("📈 Sentiment is very positive. Bullish signal! 🚀")
        elif avg_sentiment < -0.5:
            print("📉 Sentiment is very negative. Bearish signal! ⚠️")
        else:
            print("⚖️ Sentiment is neutral. Stay cautious.")

    except Exception as e:
        logger.error(f"❌ Error during sentiment analysis: {str(e)}")

# Optional: run directly
if __name__ == "__main__":
    analyze_sentiment()
