import unittest
from rating_calculator import RatingCalculator
from movie import Movie

class TestRatingCalculator(unittest.TestCase):

    def test_penalize_movies(self):
        Test2 = RatingCalculator()
        obj1 = Movie("Title1", 9.5, 800000, 0, 0.0, 0.0)
        obj2 = Movie("Title2", 8.5, 500000, 2, 0.0, 0.0)
        obj3 = Movie("Title3", 8.0, 300000, 1, 0.0, 0.0)
        li = [obj1, obj2, obj3]
        li = Test2.penalize_movies(li)
        self.assertEqual(obj2.rating_penalized, 8.2)
        self.assertEqual(obj3.rating_penalized, 7.5)

    def test_oscar_calculator(self):
        Test2 = RatingCalculator()
        obj1 = Movie("Title1", 7.5, 800000, 10, 7.5, 7.5)
        obj2 = Movie("Title2", 8.5, 500000, 2, 8.5, 8.5)
        obj3 = Movie("Title3", 6.5, 500000, 5, 6.5, 6.5)
        obj4 = Movie("Title4", 9.0, 500000, 0, 9.0, 9.0)
        li = [obj1, obj2, obj3]
        li = Test2.oscar_calculator(li)
        self.assertEqual(obj1.rating_adjusted, 8.5)
        self.assertEqual(obj2.rating_adjusted, 8.8)
        self.assertEqual(obj3.rating_adjusted, 7.0)
        self.assertEqual(obj4.rating_adjusted, 9.0)


if __name__ == '__main__':
    unittest.main()