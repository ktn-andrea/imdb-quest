class Penalizer():

    def __init__(self) -> None:
        pass

    @staticmethod
    def penalize_movies(movies):

        max_num_of_ratings = max(movie.num_of_ratings for movie in movies)

        for movie in movies:
            print(movie.rating)
            deviation = max_num_of_ratings - movie.num_of_ratings
            deduction = (deviation // 100000) * 0.1
            new_rating = round(movie.rating - deduction, 1)
            movie.rating_penalized = new_rating
            movie.rating_adjusted = new_rating
            print(movie.rating_penalized)
            print('*' * 20)
