class OscarCalculator():

    def __init__(self) -> None:
        pass

    @staticmethod
    def adjust_rating(movies):

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
                
