class Movie(object):
    
    def __init__(self, title, rating, num_of_ratings, num_of_oscar_wins, rating_penalized, rating_adjusted):
        self.title = title
        self.rating = rating
        self.num_of_ratings  = num_of_ratings
        self.num_of_oscar_wins = num_of_oscar_wins
        self.rating_penalized = rating_penalized
        self.rating_adjusted = rating_adjusted
       