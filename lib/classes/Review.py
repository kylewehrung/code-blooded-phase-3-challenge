class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

    # rating property goes here!
    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating
        else:
            raise Exception




    # viewer property goes here!

    # movie property goes here!
