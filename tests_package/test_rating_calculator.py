import unittest
from rating_calculator import RatingCalculator
from movie import Movie

class TestRatingCalculator(unittest.TestCase):

    def test_penalize_movies(self):
        Test2 = RatingCalculator()
        obj1 = Movie("title", 9.5, 800000, 0, None, None)
        obj2 = Movie("title", 8.5, 500000, 2, None, None)
        li = [obj1, obj2]
        li = Test2.penalize_movies(li)
        self.assertEqual(obj2.rating_penalized, 8.2)

    def test_oscar_calculator(self):
        Test2 = RatingCalculator()
        obj1 = Movie("title", 9.5, 800000, 0, 9.5, 9.5)
        obj2 = Movie("title", 8.5, 500000, 2, 8.5, 8.5)
        li = [obj1, obj2]
        li = Test2.oscar_calculator(li)
        self.assertEqual(obj1.rating_adjusted, 9.5)
        self.assertEqual(obj2.rating_adjusted, 8.8)


if __name__ == '__main__':
    unittest.main()