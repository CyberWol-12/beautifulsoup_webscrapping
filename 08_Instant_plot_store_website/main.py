from bs4 import BeautifulSoup
import requests
import pandas as pd

product_info = []

practise_url = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6?th=1"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

r = requests.get(practise_url)
soup = BeautifulSoup(r.content,"html.parser")

tag_info = soup.find_all("span",class_ = "a-size-large product-title-word-break")
print(tag_info)

price_tag = soup.find("p",class_ = "a-spacing-none a-text-left a-size-mini twisterSwatchPrice")
# print(price_tag.getText().strip())