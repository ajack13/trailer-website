##########################
# author Ajay
# date : 24th aug 2015
###########################

import webbrowser

#####################################################
# the parent class for Tv_series and Movie classes
# takes 4 arguments
#####################################################
class Video():
	
	def __init__(self,title,youtube_link,description,rating):
		self.title = title
		self.youtube_link = youtube_link
		self.description =description
		self.rating = rating

########################################################
# Child class of video
# takes 1 argument poster image url
########################################################
class Movie(Video):

	def __init__(self,title,youtube_link,poster_image_url,description,rating):
		Video.__init__(self,title,youtube_link,description,rating)
		self.poster_image_url = poster_image_url

########################################################
# Child class of video
# takes 2 argument poster image url and seasons
########################################################
class Tv_series(Video):

	def __init__(self,title,youtube_link,poster_image_url,description,rating,seasons):
		Video.__init__(self,title,youtube_link,description,rating)
		self.poster_image_url = poster_image_url
		self.seasons = seasons
