import os
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from movie import Movie
from scraper import Imdb_Scraper


def main():

    Imdb_scraper = Imdb_Scraper()
    uri_top_250 = "https://www.imdb.com/chart/top/"
    Imdb_Top_20 = Imdb_scraper.get_top_20(uri_top_250)

    for i in Imdb_Top_20:
        print(i.title)
        print(i.num_of_oscar_wins)
        print(i.rating)
        print(i.num_of_ratings)
    
    
main()