# 24 Web Scraper
# 24 Web Scraper
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
try:
    response = requests.get(URL, timeout=10)
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
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

cards = soup.find_all("div", class_="card-content")

jobs = []
for card in cards:
    title = card.find("h2").text.strip()
    company = card.find("h3").text.strip()
    location = card.find("p").text.strip()
    jobs.append({"title": title, "company": company, "location": location})

def filter_jobs(jobs, keyword):
    return [job for job in jobs if keyword.lower() in job["title"].lower()]

keyword = input("What job are you looking for?: ")
results = filter_jobs(jobs, keyword)

for job in results:
    print(f"{job['title']} at {job['company']} - {job['location']}")

df = pd.DataFrame(results)
df.to_csv("jobs.csv", index=False)