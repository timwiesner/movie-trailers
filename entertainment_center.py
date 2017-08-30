"""
movie_website contains a program which displays movies and their relevant information.
the movie trailer is played when the movie poster is clicked on

entertainment_center contains movie information
'python entertainment_center.py' to run

fresh_tomatoes provides html and function for opening movie trailers
media contains 'Movie' class

"""

from media import Movie
from fresh_tomatoes import open_movies_page

inside_llewyn_davis = Movie("Inside Llewyn Davis",
								  "A week in the life of a young singer as he navigates the Greenwich Village folk scene of 1961.",
								  "http://t3.gstatic.com/images?q=tbn:ANd9GcSLO-BiIX0rnumBd9eL7gIDsKlwIR9zSZc9LQxggueQi_-IPGof",
								  "http://www.imdb.com/title/tt2042568/",
								  "https://www.youtube.com/watch?v=eXMuR-Nsylg",
								  "Ethan Coen, Joel Coen",
								  "Ethan Coen, Joel Coen",
								  "Oscar Isaac, Carey Mulligan, John Goodman",
								  "2014",
								  "7.4 / 10"
								 )

inglorious_basterds = Movie("Inglorious Basterds",
								  "In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same.",
								  "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
								  "http://www.imdb.com/title/tt0361748/",
								  "https://www.youtube.com/watch?v=KnrRy6kSFF0",
								  "Quentin Tarantino",
								  "Quentin Tarantino",
								  "Brad Pitt, Diane Kruger, Eli Roth",
								  "2009",
								  "8.3 / 10"
								 )

pulp_fiction = Movie("Pulp Fiction",
						   "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
						   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
						   "http://www.imdb.com/title/tt0110912/",
						   "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
						   "Quentin Tarantino",
						   "Quentin Tarantino, Roger Avery",
						   "John Travolta, Uma Therman, Samuel L. Jackson",
						   "1994",
						   "8.9 / 10"
						  )

inception = Movie("Inception",
					    "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
					    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
					    "http://www.imdb.com/title/tt1375666/",
					    "https://www.youtube.com/watch?v=YoHD9XEInc0",
					    "Christopher Nolan",
					    "Christopher Nolan",
					    "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
					    "2010",
					    "8.8 / 10"
					   )

fight_club = Movie("Fight Club",
						 "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
						 "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
						 "http://www.imdb.com/title/tt0137523/",
						 "https://www.youtube.com/watch?v=SUXWAEX2jlg",
						 "David Fincher",
						 "Chuck Palahniuk, Jim Uhls",
						 "Brad Pitt, Edward Norton, Meat Loaf",
						 "1999",
						 "8.8 / 10"
						)

pineapple_express = Movie("Pineapple Express",
								"A process server and his marijuana dealer wind up on the run from hitmen and a corrupt police officer after he witnesses his dealer's boss murder a competitor while trying to serve papers on him.",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BMTY1MTE4NzAwM15BMl5BanBnXkFtZTcwNzg3Mjg2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
								"http://www.imdb.com/title/tt0910936/?ref_=nv_sr_1",
								"https://www.youtube.com/watch?v=wWbEoEJsxYw",
								"David Gordon Green",
								"Seth Rogen, Evan Goldberg",
								"Seth Rogan, James Franco, Gary Cole",
								"2008",
								"7.0 / 10"
							   )

movies = [inside_llewyn_davis, inglorious_basterds, pulp_fiction, inception, fight_club, pineapple_express]

open_movies_page(movies)