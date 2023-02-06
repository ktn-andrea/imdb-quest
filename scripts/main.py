#!/usr/bin/env python3.11

from scraper import Scraper
from rating_calculator import RatingCalculator
from movie import Movie
import codecs, json
import logging, timeit
import sys

def main():
    '''Scrapes data from IMDB and adjusts IMDB ratings based on some rules.
        Writes the results to an output file (results.json).'''
    
    if sys.version_info[0] != 3:
        raise Exception("Python version 3 is needed to run this program.")

    start = timeit.default_timer()
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    
    logging.info('Web scraping started...')
    ImdbScraper = Scraper()
    Imdb_Top_20 = ImdbScraper.get_top_20("https://www.imdb.com/chart/top/")

    logging.info('Adjusting ratings...')
    MovieCalculator = RatingCalculator()
    MovieCalculator.penalize_movies(Imdb_Top_20)
    MovieCalculator.oscar_calculator(Imdb_Top_20)

    logging.info('Writing results to results.json...')
    try:
        with codecs.open("results.json", "w", encoding='utf-8') as f:
            for movie in Imdb_Top_20:
                f.write(json.dumps(Movie.to_json(movie), indent=4, separators=(',', ': '), ensure_ascii=False))
    except IOError:
        logging.error("Could not write results to results.json.")

    end = timeit.default_timer()
    logging.info('Finished in: {} seconds.'.format(end-start))

    
if __name__ == "__main__":
    main()