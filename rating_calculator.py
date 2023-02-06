class RatingCalculator():

    def __init__(self) -> None:
        pass

    @staticmethod
    def penalize_movies(movies):
        max_num_of_ratings = max(movie.num_of_ratings for movie in movies)
        for movie in movies:
            deviation = max_num_of_ratings - movie.num_of_ratings
            deduction = (deviation // 100000) * 0.1
            new_rating = round(movie.rating - deduction, 1)
            movie.rating_penalized = new_rating
            movie.rating_adjusted = new_rating

    @staticmethod
    def oscar_calculator(movies):
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

        return movies
