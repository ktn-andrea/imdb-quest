from scraper import ImdbScraper
from rating_calculator import RatingCalculator
from movie import Movie
import codecs, json
import logging, timeit

def main():

    start = timeit.default_timer()
    logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)
    
    logging.info('Web scraping started...')
    Imdb_scraper = ImdbScraper()
    uri_top_250 = "https://www.imdb.com/chart/top/"
    Imdb_Top_20 = Imdb_scraper.get_top_20(uri_top_250)

    logging.info('Adjusting ratings...')
    Movie_Oscar_Calculator = RatingCalculator()
    Movie_Oscar_Calculator.penalize_movies(Imdb_Top_20)
    Movie_Oscar_Calculator.oscar_calculator(Imdb_Top_20)

    logging.info('Writing results to results.json...')
    with codecs.open("results.json", "w", encoding='utf-8') as f:
        for movie in Imdb_Top_20:
            f.write(json.dumps(Movie.to_json(movie), indent=4, separators=(',', ': '), ensure_ascii=False))

    end = timeit.default_timer()
    logging.info('Finished in: {} seconds.'.format(end-start))

    

main()