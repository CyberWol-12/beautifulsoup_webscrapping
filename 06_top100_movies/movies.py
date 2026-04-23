import requests
from bs4 import BeautifulSoup
import pandas as pd

product_list = []


baseurl = "https://www.empireonline.com"
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
songs_list = soup.find_all("div",class_ = "article-title-description__text")

for item in songs_list:
    #movies title
    movie_tag = item.find("h3",class_ = "title").text.strip()
    # in which year the movie released
    year_tag = item.find("strong")
    if year_tag:
        year = year_tag.getText().strip()
    else:
        year = None
    print(year)   
    #link tag here we use review link and full link both
    link_tag = item.find("a",href = True)
    relative_link = link_tag['href']
    full_link = baseurl + relative_link
    #we can create 2 variable so that we can call both link independent way 
    review_link  = relative_link
    complete_link = full_link
    # now we create dictionary so that we can store all items in dict
    data_dict = {
        "Movie":movie_tag,
        "Year":year,
        "Review_link":review_link,
        "full_link":complete_link
    }
    product_list.append(data_dict)

df = pd.DataFrame(product_list)
df.to_csv("top100_movies.csv",index = False)
    












