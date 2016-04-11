__author__ = "Petra Sargent"

import webbrowser

class Video():
    """ This is the Parent class that stores the titles and story lines/descriptions of videos.

    Attributes:
        title: A string indicating the title of the movie
        storyline: A string that describes the story line of a movie

    """
    def __init__(self, title, storyline):
        self.title = title
        self.storyline = storyline  


class Movie(Video):
    """ This class stores  movie ratings, movie release dates, movie cast, image of movie poster and
        a YouTube link to the movie trailer. This class inherites title attribute and storyline attribe
        from the Video class.

    Attributes:
        title: inherited from Video class
        movie_rating: Indicates the movie rating
        storyline: Inherited from Video class
        movie_release_date: Indicates the date the movie was released to the public
        movie_cast: the names of the actors and actresses of the movie
        poster_image: A image of movie poster
        trailer_youtube: a YouTube link to the movie trailer
    """
    
    def __init__(self, title, movie_rating, storyline, movie_release_date, movie_cast, poster_image, trailer_youtube):
        Video.__init__(self, title, storyline)
        self.title = title
        self.rating = movie_rating
        self.release_date = movie_release_date
        self.cast = movie_cast
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


