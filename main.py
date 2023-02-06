from scraper import ImdbScraper
from rating_calculator import RatingCalculator
from movie import Movie
import codecs, json

def main():

    Imdb_scraper = ImdbScraper()
    uri_top_250 = "https://www.imdb.com/chart/top/"
    Imdb_Top_20 = Imdb_scraper.get_top_20(uri_top_250)

    Movie_Oscar_Calculator = RatingCalculator()
    Movie_Oscar_Calculator.penalize_movies(Imdb_Top_20)
    Movie_Oscar_Calculator.oscar_calculator(Imdb_Top_20)

    with codecs.open("results.json", "w", encoding='utf-8') as f:
        for movie in Imdb_Top_20:
            f.write(json.dumps(Movie.to_json(movie), indent=4, separators=(',', ': '), ensure_ascii=False))
    

    

main()