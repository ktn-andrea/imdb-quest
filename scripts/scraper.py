#!/usr/bin/env python3.11

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from movie import Movie
from typing import List

class Scraper():
    
    def __init__(self) -> None:
        pass

    def get_top_20(self, top_250: List[object]) -> List[object]:
        '''Scrapes the IMDB TOP 250 web page and returns the first 20 movies.
            Scrapes four properties of the movies: 
                - title
                - rating
                - number of rating
                - number of Oscars -> scrapes seperately from the web page of the given movie'''
        req_top_250 = Request(top_250 , headers={'User-Agent': 'Mozilla/5.0'})
        soup_top_250 = BeautifulSoup(urlopen(req_top_250).read(), 'html.parser')

        titles_top_20 = soup_top_250.find_all('td', class_= 'titleColumn')[:20]
        ratings_top_20 = soup_top_250.find_all('td', class_= 'ratingColumn imdbRating')[:20]

        Imdb_Top_20 = []

        for title_item, rating_item in zip(titles_top_20, ratings_top_20):
            title = title_item.findChild('a').get_text()
            ratings_string = rating_item.findChild('strong')['title']
            rating = float(ratings_string.split()[0])
            num_of_ratings = int(ratings_string.split()[3].replace(',', '')) 

            movie_uri = "https://imdb.com" + str(title_item.findChild('a', href=True)['href'])
            oscars = self.get_oscar_wins(movie_uri)
            
            movie = Movie(title, rating, num_of_ratings, oscars, 0, 0)
            Imdb_Top_20.append(movie)

        return Imdb_Top_20

    @staticmethod
    def get_oscar_wins(uri: str()) -> int():
        '''Scrapes the number of Oscars from the web page of a given movie.'''
        req_movie = Request(uri , headers={'User-Agent': 'Mozilla/5.0'})
        soup_movie = BeautifulSoup(urlopen(req_movie).read(), "html.parser")

        awards = soup_movie.find('div', attrs={"data-testid": "awards"})
        oscars = awards.findChild('a', attrs={"role" : "button", "class": "ipc-metadata-list-item__label ipc-metadata-list-item__label--link"}).get_text()
        oscar_wins = int(oscars.split()[1]) if "Won" in oscars and "Oscar" in oscars else 0

        return oscar_wins
    
    
