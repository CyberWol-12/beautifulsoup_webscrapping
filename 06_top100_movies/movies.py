from bs4 import BeautifulSoup
import requests
import pandas as pd

movies_info = []

url = "https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

r = requests.get(url, headers=headers)
website_html = r.text

soup = BeautifulSoup(website_html, "html.parser")


title_info = soup.find_all("h3",class_ ="title")

movie_title = [movie.getText() for movie in title_info]
print(movie_title)

