import media
import fresh_tomatoes

# creating movie instance
batman_begins = media.Movie('Batman Begins',
							'https://www.youtube.com/watch?v=iw_CphigcOo',
							'https://www.movieposter.com/posters/archive/main/80/MPW-40279',
							'After training with his mentor, Batman begins his war on crime to free the crime-ridden Gotham City',
							'8.3')



the_dark_knight = media.Movie('The Dark Knight',
							'https://www.youtube.com/watch?v=EXeTwQWrcwY',
							'http://orig05.deviantart.net/25af/f/2007/259/a/a/the_dark_knight_movie_poster_by_ff001.jpg',
							'When the Joker wreaks chaos on the people of Gotham, the caped crusader must defeat him ',
							'9.0')


the_dark_knight_rises = media.Movie('The Dark Knight Rises',
							'https://www.youtube.com/watch?v=g8evyE9TuYk',
							'https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61c8e4b0d911b44a0a49/1339033375837/1000w/TDKRPoster7.jpg',
							'The Dark Knight is forced to return from his imposed exile to save Gotham City from the brutal guerrilla terrorist Bane',
							'8.5')

# array of movie instances
movies = [batman_begins,the_dark_knight,the_dark_knight_rises]

# creating tvseries instance
batman_the_animated_series = media.Tv_series('Batman The Series',
											'https://www.youtube.com/watch?v=OxGGaFhKEOM',
											'http://richlunghino.com/images/full/batmantas_poster.jpg',
											'The Dark Knight battles crime in Gotham City with occasional help from Robin and Batgirl.',
											'9.0',
											'4'
											)

batman_beyond = media.Tv_series('Batman Beyond',
											'https://www.youtube.com/watch?v=bqhsoAGsOXE',
											'http://images.moviepostershop.com/batman-beyond---return-of-the-joker-movie-poster-2000-1010474037.jpg',
											'Fueled by remorse and vengeance, a high schooler named Terry McGinnis revives the role of Batman.',
											'8.3',
											'2'
											)

batman = media.Tv_series('Batman',
							'https://www.youtube.com/watch?v=whgBnumr3QQ',
							'http://3.bp.blogspot.com/-1GSKRpPgaHY/U8mBt8ZT6tI/AAAAAAAAf-Y/ObFzsj3KdA8/s1600/blu-ray-1966-batman-complete-tv-series.jpg',
							'The Caped Crusader battles evildoers in Gotham City in a bombastic 1960s parody of the comic book hero\'s exploits.',
							'7.5',
							'3'
							)


# array of tv series instances
tv_series = [batman_the_animated_series,batman_beyond,batman]

#calling method open_movies_page from fresh_tomatoes.py
fresh_tomatoes.open_movies_page([movies,tv_series]) 