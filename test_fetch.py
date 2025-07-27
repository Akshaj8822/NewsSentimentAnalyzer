from scripts.fetch_news import fetch_news

articles = fetch_news()
print("✅ Final fetched article titles:")
for article in articles:
    print("•", article['title'])
