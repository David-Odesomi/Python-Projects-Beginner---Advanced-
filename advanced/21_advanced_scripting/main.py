# 21 Advanced Scriptingpip3 install requests
import requests
from datetime import datetime
today = datetime.today().strftime("%Y-%m-%d")
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://www.alphavantage.co/query"

ticker = input("Enter stock ticker: ").upper()

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": ticker,
    "apikey": API_KEY
}

try:
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
except requests.exceptions.ConnectionError:
    print("❌ No internet connection.")
    exit()
except requests.exceptions.Timeout:
    print("❌ Request timed out.")
    exit()
except requests.exceptions.HTTPError as e:
    print(f"❌ HTTP error: {e}")
    exit()

print(response.json())

data = response.json()
if "Time Series (Daily)" not in data:
    print(f"❌ Could not fetch data. Response: {data}")
    exit()

time_series = data["Time Series (Daily)"]
today_data = time_series[today]

open_price = today_data["1. open"]
high = today_data["2. high"] 
low = today_data["3. low"]
close = today_data["4. close"]
volume = today_data["5. volume"]

print(open_price)