from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(article):
    try:
        text = f"{article.get('title', '')} {article.get('description', '')}"
        score = analyzer.polarity_scores(text)
        return {
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "publishedAt": article.get("publishedAt", ""),
            "sentiment": "positive" if score["compound"] > 0.05 else "negative" if score["compound"] < -0.05 else "neutral",
            "score": score["compound"]
        }
    except Exception as e:
        print(f"Error: {e}")
        return {}
