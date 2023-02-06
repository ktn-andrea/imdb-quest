#!/usr/bin/env python3.11

from typing import List

class RatingCalculator():

    def __init__(self) -> None:
        pass

    @staticmethod
    def penalize_movies(movies: List[object]) -> None:
        '''Takes a List of (Movie) objects, calculates their penalized ratings and initializes their adjusted ratings to the same value.
            Penalized rating is calculated by comparing the number of ratings to the maximum number of ratings(this is the benchmark).
            Every 100.000 deviation from the maximum translates to a point deduction of 0.1.'''
        max_num_of_ratings = max(movie.num_of_ratings for movie in movies)
        for movie in movies:
            deviation = max_num_of_ratings - movie.num_of_ratings
            deduction = (deviation // 100000) * 0.1
            new_rating = round(movie.rating - deduction, 1)
            movie.rating_penalized = new_rating
            movie.rating_adjusted = new_rating

    @staticmethod
    def oscar_calculator(movies: List[object]) -> None:
        '''Takes a List of (Movie) objects and calculates their adjusted ratings.
            The adjusted rating is raised based on the number of Oscars the movie has won.'''
        for movie in movies:
            point = 0
            if movie.num_of_oscar_wins in [1, 2]:
                point = 0.3
            elif movie.num_of_oscar_wins in [3, 5]:
                point = 0.5
            elif movie.num_of_oscar_wins >= 6 and movie.num_of_oscar_wins <= 10:
                point = 1.0
            elif movie.num_of_oscar_wins > 10:
                point = 1.5
            movie.rating_adjusted += point


