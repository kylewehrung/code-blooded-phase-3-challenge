from classes.Review import Review


class Viewer:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._username

    def set_username(self, username):
        if isinstance(username, str) and 6 <= len(username) <= 16:
            self._username = username
        # else:
        #     raise Exception("Username must be a string between 6-16 charachters")

    username = property(get_username, set_username)



    def reviews(self):
        from classes.Review import Review
        return [review for review in Review.all if review.viewer == self]


    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]


    def movie_reviewed(self, movie):
        return [review for review in self.reviews() if review.movie == movie]


    def rate_movie(self, movie, rating):
        pass
