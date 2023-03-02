from classes.Review import Review


class Movie:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        # else:
        #     raise Exception("Title must be a string greater than 0 charachters")

    title = property(get_title, set_title)



    def reviews(self):
        from classes.Review import Review
        return [review for review in Review.all if review.movie == self]


    def reviewers(self):
        return [review.viewer for review in self.reviews()]


    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
