import os
from dotenv import load_dotenv
import pandas as pd
from pymongo import MongoClient
import sqlite3

load_dotenv()

# MongoDB details
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "sentimentDB"
COLLECTION = "headlines"

# Use Mongo if URI is provided
USE_MONGO = True if MONGO_URI else False

def save_data(data_dict):
    if USE_MONGO:
        try:
            client = MongoClient(MONGO_URI)
            db = client[DB_NAME]
            db[COLLECTION].insert_many(data_dict)
            print("[MONGO] Data saved.")
        except Exception as e:
            print(f"[MONGO ERROR] {e}")
    else:
        try:
            # Safe path using os.path.join
            db_path = os.path.join("storage", "sentiment.db")
            conn = sqlite3.connect(db_path)
            df = pd.DataFrame(data_dict)
            df.to_sql("headlines", conn, if_exists="append", index=False)
            print("[SQLITE] Data saved.")
        except Exception as e:
            print(f"[SQLITE ERROR] {e}")
