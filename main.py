from scraper import ImdbScraper
from penalizer import Penalizer
from oscar_calculator import OscarCalculator


def main():

    Imdb_scraper = ImdbScraper()
    uri_top_250 = "https://www.imdb.com/chart/top/"
    Imdb_Top_20 = Imdb_scraper.get_top_20(uri_top_250)

    Movie_Penalizer = Penalizer()
    Movie_Penalizer.penalize_movies(Imdb_Top_20)

    Movie_Oscar_Calculator = OscarCalculator()
    Movie_Oscar_Calculator.adjust_rating(Imdb_Top_20)


    for i in Imdb_Top_20:
        print(i.title)
        print(i.num_of_oscar_wins)
        print(i.rating)
        print(i.num_of_ratings)
        print(i.rating_penalized)
        print(i.rating_adjusted)
        print('*' * 20)
    

main()