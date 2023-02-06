import unittest
from scraper import Scraper
from movie import Movie
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class TestScraper(unittest.TestCase):

    def test_get_top_20(self):
        Test = Scraper()
        url = "https://www.imdb.com/chart/top/"
        li = Test.get_top_20(url)
        self.assertTrue(len(li))

        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(req).read(), 'html.parser')
        self.assertIsNotNone(soup)

        titles = soup.find_all('td', class_= 'titleColumn')
        ratings = soup.find_all('td', class_= 'ratingColumn')
        self.assertIsNotNone(titles)
        self.assertIsNotNone(ratings)

        self.assertTrue(len(titles[0]))
        self.assertIsNotNone(str(titles[0].findChild('a', href=True)['href']))

        test_obj = Movie(titles[0], ratings[0], 1234567, 1, None, None)
        self.assertIsNotNone(test_obj)
        self.assertIsInstance(test_obj, Movie)

        
    def test_get_oscar_wins(self):
        Test = Scraper()
        url = "https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=2N5QQMRP4K2N257VP16F&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1"
        num = Test.get_oscar_wins(url)
        self.assertTrue(0 <= num)

        
if __name__ == '__main__':
    unittest.main()