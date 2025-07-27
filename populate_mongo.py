import requests
import pymongo
from datetime import datetime
import os

# MongoDB setup
MONGO_URI = "mongodb+srv://akshajdixit02:Project12@cluster0.zmwsjcx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "SentimentDB"
COLLECTION_NAME = "headlines"

# News API key
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "16e62d29a0ad49788eff3f4b688491d3")

def fetch_news():
    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category=business&language=en&pageSize=10&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        print("❌ Failed to fetch news:", response.status_code, response.text)
        return []
    
    articles = response.json().get("articles", [])
    news_data = []
    for article in articles:
        news_data.append({
            "title": article["title"],
            "description": article["description"],
            "publishedAt": article["publishedAt"],
            "source": article["source"]["name"],
            "url": article["url"],
            "fetchedAt": datetime.utcnow()
        })
    return news_data

def populate_mongo():
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        news_articles = fetch_news()

        inserted_count = 0
        for article in news_articles:
            # Avoid duplicate insertions (based on title + source)
            if not collection.find_one({"title": article["title"], "source": article["source"]}):
                collection.insert_one(article)
                inserted_count += 1
        
        if inserted_count > 0:
            print(f"✅ Inserted {inserted_count} new articles.")
        else:
            print("ℹ️ No new articles to insert (all are duplicates).")

    except Exception as e:
        print("❌ Error connecting to MongoDB or inserting data:", e)

if __name__ == "__main__":
    populate_mongo()
