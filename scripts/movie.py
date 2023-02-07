#!/usr/bin/env python3.11

class Movie(object):

    __slots__ = ['title', 'rating', 'num_of_ratings', 'num_of_oscar_wins', 'rating_penalized', 'rating_adjusted']
    
    def __init__(self, title: str, rating: float, num_of_ratings: int, num_of_oscar_wins: int, rating_penalized: float, rating_adjusted: float):
        self.title = title
        self.rating = rating
        self.num_of_ratings  = num_of_ratings
        self.num_of_oscar_wins = num_of_oscar_wins
        self.rating_penalized = rating_penalized
        self.rating_adjusted = rating_adjusted

    def to_json(self):
        '''Generates Json by extracting key-value pairs of the objects.'''
        return {key : getattr(self, key, None) for key in self.__slots__}
    
       