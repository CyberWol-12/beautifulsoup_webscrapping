from bs4 import BeautifulSoup
import pandas as pd
import requests

billboard_info  = []
website  = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

# user_asked = input("Which year do you want to travel to?Type the date in this formate YYYY-MM-DD:")
r = requests.get(website)
soup = BeautifulSoup(r.content,"html.parser")

song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")]
print(song_names)

