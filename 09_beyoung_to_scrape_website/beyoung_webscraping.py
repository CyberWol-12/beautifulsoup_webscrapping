import pandas as pd
from bs4 import BeautifulSoup
import requests

product_links = []
product_item = []

baseurl = "https://www.beyoung.in/"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
for x in range(1,10):
    url = (f"https://www.beyoung.in/mens-new-arrival?page={x}")

    r = requests.get(url)

    soup = BeautifulSoup(r.content,"html.parser")

    product_tag = soup.find_all("div",class_ = "products")

    for item in product_tag:
        for link in item.find_all("a",href = True):
            product_links.append(baseurl +link['href'])


# testlink = "https://www.beyoung.in/dusty-olive-dual-pocket-corduroy-shirt"
for link in product_links:
    r = requests.get(link,headers=headers)

    soup = BeautifulSoup(r.content,"html.parser")
    # product name
    product_name = soup.find('h1').text.strip()
    # discounted price
    discounted_price = soup.find("span",class_ = "realprice").text.strip()
    # regular price
    regular_price = soup.find("span",class_ = "cuttinprice").text.strip()
    #discount
    discount = soup.find("div",class_ = "slanted-box").text.strip()


    product_data = {
        "Product_Name":product_name,
        "Discounted_Price":discounted_price,
        "Regular_price":regular_price,
        "Discount":discount,
        "link":link
    }
    product_item.append(product_data)

    df = pd.DataFrame(product_item)
    df.to_csv("product_info.csv",index = False)


       

