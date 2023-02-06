from scraper import Imdb_Scraper
from penalizer import Penalizer

def main():

    Imdb_scraper = Imdb_Scraper()
    uri_top_250 = "https://www.imdb.com/chart/top/"
    Imdb_Top_20 = Imdb_scraper.get_top_20(uri_top_250)

    Movie_Penalizer = Penalizer()
    Movie_Penalizer.penalize_movies(Imdb_Top_20)

    for i in Imdb_Top_20:
        print(i.title)
        print(i.num_of_oscar_wins)
        print(i.rating)
        print(i.num_of_ratings)
        print(i.rating_penalized)
        print('*' * 20)
    

main()