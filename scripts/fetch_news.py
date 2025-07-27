import os
import requests
import pandas as pd
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news(query="stocks", language="en", page_size=50):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "pageSize": page_size,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])

        headlines = [{
            "title": article["title"],
            "description": article["description"],
            "publishedAt": article["publishedAt"],
            "source": article["source"]["name"]
        } for article in articles]

        df = pd.DataFrame(headlines)
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/headlines.csv", index=False)
        logger.info(f"Fetched and saved {len(df)} headlines.")
    else:
        logger.error(f"Failed to fetch news: {response.status_code}")
        print("Error fetching news:", response.status_code)
 
def fetch_news():
    print("🔍 Starting news fetch...")
    
    # Example: Using NewsAPI
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "stock market",
        "apiKey": "16e62d29a0ad49788eff3f4b688491d3",
        "language": "en",
        "pageSize": 5
    }
    
    response = requests.get(url, params=params)
    print(f"🔄 NewsAPI Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("❌ Failed to fetch news.")
        return []

    data = response.json()
    print(f"📰 Articles fetched: {len(data.get('articles', []))}")
    
    return data.get("articles", [])

    print(f"Fetched {len(results)} articles")
    return results

