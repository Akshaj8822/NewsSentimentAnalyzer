# 📰 News Sentiment Analyzer

[![Streamlit App](https://img.shields.io/badge/Built%20With-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Made%20With-Python-3670A0?logo=python&logoColor=white)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A simple web app that performs real-time sentiment analysis on news headlines using Streamlit and MongoDB.

---
### A look how the webpages look like

<img width="951" height="466" alt="image" src="https://github.com/user-attachments/assets/9f069fd1-4cf7-4ae6-879e-4216c5491fd5" />

<img width="952" height="480" alt="image" src="https://github.com/user-attachments/assets/4cdeb276-aa51-47d9-b747-37f3bc7ef38e" />

---

## 🛠️ Features

- 🔍 Scrapes news headlines from a JSON or CSV source
- 🤖 Performs sentiment analysis (Positive/Negative/Neutral)
- 🧠 Uses `vaderSentiment` for scoring
- 💾 Stores analysis in MongoDB
- 📊 Displays result in a clean Streamlit UI

## 📂 Project Structure

```
news-sentiment-analyzer/
├── backend/
│   ├── app.py                  # Main backend logic
│   ├── config.py               # DB configuration
│   ├── news_sentiment.py       # Sentiment analysis logic
│   └── requirements.txt        # Python dependencies
├── .env                        # MongoDB URI stored securely
├── streamlit_app.py            # Frontend app
├── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/news-sentiment-analyzer.git
cd news-sentiment-analyzer
```

### 2. Setup Environment

Install required packages (preferably in a virtual environment):

```bash
pip install -r backend/requirements.txt
```

### 3. Configure `.env`

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb://localhost:27017
```

### 4. Run the Backend (Optional: Only if testing separately)

```bash
python backend/app.py
```

### 5. Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

## 📊 Output Preview

| 📰 Headline | 😃 Sentiment |
|------------|--------------|
| "Markets rally after rate cut" | ✅ Positive |
| "Investors unsure about inflation" | 😐 Neutral |
| "Stocks plunge amid crisis fears" | ❌ Negative |

---

## 🔧 Tech Stack

- **Python 3.8+**
- **Streamlit**
- **VADER Sentiment Analyzer**
- **MongoDB**
- **Pandas**

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

Made with ❤ by [Akshaj Dixit](https://github.com/Akshaj8822)  
Feel free to ⭐ the repo if you found it useful!

