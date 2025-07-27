import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import sqlite3
from pymongo import MongoClient

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "sentimentDB")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "sentiments")
USE_MONGO = True if MONGO_URI else False

# Streamlit page setup
st.set_page_config(page_title="News Sentiment Dashboard", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .css-1v0mbdj { font-size:18px; }
        .css-18ni7ap { background-color: #f0f2f6; padding: 20px; border-radius: 10px; }
        .stApp { background-color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

st.title("📰 Real-Time News Sentiment Analysis")

# Fetch data from DB
try:
    if USE_MONGO:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]
        data = list(collection.find({}, {"_id": 0}))  # exclude Mongo's _id field
        df = pd.DataFrame(data)
    else:
        conn = sqlite3.connect(os.path.join("storage", "sentiment.db"))
        df = pd.read_sql_query("SELECT * FROM sentiments", conn)

    if not df.empty:
        df['publishedAt'] = pd.to_datetime(df['publishedAt'])
        st.write(f"🔄 Last update: {df['publishedAt'].max()}")

        st.dataframe(df[['title', 'source', 'sentiment']].sort_values(by="sentiment", ascending=False), use_container_width=True)

        avg_sentiment = df['sentiment'].mean()
        st.metric("📊 Average Sentiment Score", f"{avg_sentiment:.3f}")

        st.bar_chart(df['sentiment'])
    else:
        st.warning("No data found in the database.")

except Exception as e:
    st.error(f"Error loading data from database: {e}")
