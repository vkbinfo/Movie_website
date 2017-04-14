class Video():
    def __init__(self,title):
        self.title=title





class Movie(Video):
    def __init__(self,movie_title,movie_storyline,movie_image_url,movie_trailer_url):
        Video.__init__(self,movie_title)
        self.storyLine=movie_storyline
        self.poster_image_url=movie_image_url
        self.trailer_youtube_url=movie_trailer_url







