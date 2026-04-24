import pandas as pd
from bs4 import BeautifulSoup
import requests

product_links = []
product_item = []

baseurl = "https://www.beyoung.in/"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
for x in range(1,51):
    url = (f"https://www.beyoung.in/mens-new-arrival?page={x}")

    r = requests.get(url)

    soup = BeautifulSoup(r.content,"html.parser")

    product_tag = soup.find_all("div",class_ = "products")

    for item in product_tag:
        for link in item.find_all("a",href = True):
            product_links.append(baseurl +link['href'])
 
       

