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
    ImdbTop20 = ImdbScraper.get_top_20()

    logging.info('Adjusting ratings...')
    MovieCalculator = RatingCalculator()
    MovieCalculator.penalize_movies(ImdbTop20)
    MovieCalculator.oscar_calculator(ImdbTop20)

    logging.info('Writing results to results.json...')
    try:
        with codecs.open("results.json", "w", encoding='utf-8') as f:
            jsonStr = []
            for movie in ImdbTop20:
                jsonStr.append(Movie.to_json(movie))
            f.write(json.dumps(jsonStr, separators=(',', ': '), indent=4, ensure_ascii=False))
    except IOError:
        logging.error("Could not write results to results.json.")

    end = timeit.default_timer()
    logging.info('Finished in: {} seconds.'.format(end-start))

    
if __name__ == "__main__":
    main()