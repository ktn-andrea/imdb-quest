import unittest
from scraper import Scraper
from movie import Movie
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class TestScraper(unittest.TestCase):

    def test_get_top_20(self):
        Test = Scraper()
        test_url = "https://www.imdb.com/chart/top/"
        test_li = Test.get_top_20()
        self.assertTrue(len(test_li))

        req = Request(test_url , headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(req).read(), 'html.parser')
        self.assertIsNotNone(soup)

        test_titles = soup.find_all('td', class_= 'titleColumn')
        test_ratings = soup.find_all('td', class_= 'ratingColumn')
        self.assertIsNotNone(test_titles)
        self.assertIsNotNone(test_ratings)

        self.assertTrue(len(test_titles[0]))
        self.assertIsNotNone(str(test_titles[0].findChild('a', href=True)['href']))

        test_obj = Movie(test_titles[0], test_ratings[0], 1234567, 1, 0.0, 0.0)
        self.assertIsNotNone(test_obj)
        self.assertIsInstance(test_obj, Movie)

        
    def test_get_oscar_wins(self):
        Test = Scraper()
        test_movie_url = "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=2N5QQMRP4K2N257VP16F&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1"
        test_num = Test.get_oscar_wins(test_movie_url)
        self.assertTrue(test_num >= 0)

        
if __name__ == '__main__':
    unittest.main()