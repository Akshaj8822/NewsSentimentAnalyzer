# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sqlite3
from pymongo import MongoClient
from dotenv import load_dotenv
from scripts.fetch_news import fetch_news
from sentiment import analyze_sentiment

load_dotenv()

st.set_page_config(layout="wide", page_title="Quant Sentiment Tracker")

st.title("📰 News Sentiment Analysis Dashboard")

# Mongo or SQLite
MONGO_URI = os.getenv("MONGO_URI")
USE_MONGO = True if MONGO_URI else False

def load_data():
    if USE_MONGO:
        try:
            client = MongoClient(MONGO_URI)
            db = client["SentimentDB"]  # lowercase name
            data = list(db["headlines"].find({}, {"_id": 0}))
            return pd.DataFrame(data)
        except Exception as e:
            st.error(f"MongoDB Error: {e}")
            return pd.DataFrame()
    else:
        try:
            conn = sqlite3.connect("sentiment.db")  # lowercase filename
            return pd.read_sql("SELECT * FROM headlines", conn)
        except Exception as e:
            st.error(f"SQLite Error: {e}")
            return pd.DataFrame()

def refresh_data():
    st.info("🔄 Fetching latest news and updating sentiment...")

    news = fetch_news()
    if not news:
        st.warning("No news articles fetched.")
        return

    results = [analyze_sentiment(article) for article in news]
    df = pd.DataFrame(results)

    if USE_MONGO:
        client = MongoClient(MONGO_URI)
        db = client["SentimentDB"]  # lowercase name
        db["headlines"].delete_many({})  # Clean old data
        db["headlines"].insert_many(df.to_dict("records"))
    else:
        conn = sqlite3.connect("sentiment.db")  # lowercase filename
        c = conn.cursor()
        c.execute("DELETE FROM headlines")  # Clean old data
        df.to_sql("headlines", conn, if_exists="append", index=False)
        conn.commit()
        conn.close()

    st.success("✅ News and sentiment data refreshed!")

# Button to refresh news
if st.button("🔄 Refresh News Sentiment Data"):
    refresh_data()

# Load and display data
df = load_data()

if df.empty:
    st.warning("No data available.")
else:
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    df = df.sort_values("publishedAt", ascending=False)

    st.subheader("🔎 Latest Headlines")
    st.dataframe(df[["title", "sentiment", "score", "publishedAt"]].head(10), height=300)

    st.subheader("📈 Sentiment Score Over Time")
    df_daily = df.groupby(df["publishedAt"].dt.date)["score"].mean().reset_index()
    df_daily.columns = ["Date", "Average Score"]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df_daily["Date"], df_daily["Average Score"], marker="o", color="teal")
    ax.axhline(0.5, ls="--", color="green", label="Bullish Threshold")
    ax.axhline(-0.5, ls="--", color="red", label="Bearish Threshold")
    ax.set_title("Average Daily Sentiment")
    ax.legend()
    st.pyplot(fig)

    st.markdown("💾 Data Source: NewsAPI.org | 💡 Built with VADER NLP")
