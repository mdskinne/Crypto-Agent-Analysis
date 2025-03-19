# Crypto-Data-Analysis
This is a **Flask-based web application** that allows users to **fetch historical cryptocurrency data and generate an analysis report** using AI-driven research and reporting agents. Research agent and reporting agent work together in a simple crypto analysis based on and using Open AI Agents SDK.

---

## 🚀 Features
- **Fetches real-time cryptocurrency historical data**
- **AI-powered analysis of market trends**
- **Simple web interface running on `localhost`**
- **Asynchronous processing with Flask & asyncio**

---

## 🛠️ Installation & Setup

### **1️ Clone the Repository**


```bash
git clone https://github.com/mdskinne/crypto-data-analysis.git
cd crypto-data-analysis
```

### **2️ Set Up a Virtual Environment (Optional, Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3 API KEYS**
Embed OpenAI API Key into the Environment
```bash
$env:OPENAI_API_KEY = "your api key"
```

### **4 Install Dependencies**

```bash
pip install -r requirements.txt
```


### Utilize Financial Datasets AI API Key to get Crypto Data
Name this file financialdatasets.py


```
import requests

FIN_API_KEY = "your api key"

def fetch_crypto_prices(ticker, interval="day", interval_multiplier=1, start_date="2024-01-01", end_date="2025-03-18"):
    headers = {"X-API-KEY": FIN_API_KEY}
    params = {
        "ticker": ticker,
        "interval": interval,
        "interval_multiplier": interval_multiplier,
        "start_date": start_date,
        "end_date": end_date
    }
    url = "https://api.financialdatasets.ai/crypto/prices/"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json().get("prices", [])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
```

## 🌍 Running the Web App
After installing dependencies, start the Flask app with:

```bash
python app.py
```

Once running, open your browser and go to:
👉 **http://127.0.0.1:5000**

---

## 🎯 How to Use
1. **Enter a cryptocurrency symbol** (e.g., `BTC-USD` or `ETH-USD`).
2. **Click "Analyze"** to fetch and analyze historical data.
3. **View the AI-generated report** directly in the browser.

---

## 🛠️ Project Structure

```bash
/crypto-analysis-webapp
│── /templates
│   └── index.html    # Frontend UI
│── app.py           # Flask web server
│── research_agent.py # AI-powered research agent
│── reporting_agent.py # AI-powered reporting agent
│── requirements.txt  # List of dependencies
│── README.md        # Project documentation
|__financialdatsets.py #Downloads crypto data using API
```

---

## 💡 Future Enhancements
- ✅ **Add data visualization (charts & graphs)**
- ✅ **Support multiple cryptocurrencies at once**
- ✅ **Improve AI-generated insights**

---

## 📝 License
This project is licensed under the **MIT License**.

---


