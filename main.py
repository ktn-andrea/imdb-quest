import os
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen



def main():
    
    uri_top_250 = "https://www.imdb.com/chart/top/"
    req_top_250 = Request(uri_top_250 , headers={'User-Agent': 'Mozilla/5.0'})
    soup_top_250 = BeautifulSoup(urlopen(req_top_250).read(), 'html.parser')

    titles_top_20 = soup_top_250.find_all('td', class_= 'titleColumn')[:20]
    ratings_top_20 = soup_top_250.find_all('td', class_= 'ratingColumn imdbRating')[:20]
    
    Imdb_Top_20 = []

    for title_item in titles_top_20:

        title = title_item.findChild('a').get_text()

        print(title)
        


        


main()