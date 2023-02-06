from scraper import ImdbScraper
from rating_calculator import RatingCalculator


def main():

    Imdb_scraper = ImdbScraper()
    uri_top_250 = "https://www.imdb.com/chart/top/"
    Imdb_Top_20 = Imdb_scraper.get_top_20(uri_top_250)

    Movie_Oscar_Calculator = RatingCalculator()
    Movie_Oscar_Calculator.penalize_movies(Imdb_Top_20)
    Movie_Oscar_Calculator.oscar_calculator(Imdb_Top_20)


    for i in Imdb_Top_20:
        print(i.title)
        print(i.num_of_oscar_wins)
        print(i.rating)
        print(i.num_of_ratings)
        print(i.rating_penalized)
        print(i.rating_adjusted)
        print('*' * 20)
    

main()