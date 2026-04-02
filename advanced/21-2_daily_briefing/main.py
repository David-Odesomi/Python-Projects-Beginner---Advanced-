# 22 Daily Briefing
import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_KEY = os.getenv("API_KEY")

params = {
    "q": "Abuja",
    "appid": WEATHER_KEY,
    "units": "metric"
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
data = response.json()

print(data)