import os
from pymongo import MongoClient
from dotenv import load_dotenv
from sentiment import analyze_sentiment

# Load environment variables
load_dotenv()

# Updated MongoDB URI and database details
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "SentimentDB"  # Update this
COLLECTION_NAME = "headlines"  # Update this

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def get_news():
    articles = list(collection.find())
    for article in articles:
        content = article.get("description", "") or article.get("content", "")
        article["sentiment"] = analyze_sentiment(content)
    return articles
