"""This file creates 'Movie' class for use by 'entertainment_center'"""

import webbrowser

class Movie():
	"""Stores movie-related information 
		
	Args:
		param1 (str): title
		param2 (str): storyline
		param3 (str): poster
		param4 (str): imdb_link
		param5 (str): trailer
		param6 (str): director/s
		param7 (str): screenwriter/s
		param8 (str): stars
		param9 (str): release date
		param10 (str): IMDB Rating

	"""

	def __init__(self, movie_title, movie_storyline, poster_image, imdb_link, trailer_youtube, directors, screenwriters, stars, release_date, imdb_rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.imdb_link_url = imdb_link
		self.trailer_youtube_url = trailer_youtube
		self.directors = directors
		self.screenwriters = screenwriters
		self.stars = stars
		self.release_date = release_date
		self.imdb_rating = imdb_rating

	# def show_trailer(self):
	# 	"""Shows movie trailer

	# 	Args:
	# 		param: self(movie)
	# 	Behavior:
	# 		Opens movie trailer in webbrowser
	# 	Returns:
	# 		None

	# 	"""
	# 	webbrowser.open(self.trailer_youtube_url)