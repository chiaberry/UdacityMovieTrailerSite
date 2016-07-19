# Creates a class Movie, which stores a title,
# film description, and links to movie poster and
# youtube trailer


class Movie(object):

    '''
    Class to store Movie data, including Title,
    Description, Poster image URL, and Trailer URL on Youtube

    All data stored as strings.

    '''
    def __init__(self, movie_title, movie_description,
                 poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.movie_description = movie_description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
