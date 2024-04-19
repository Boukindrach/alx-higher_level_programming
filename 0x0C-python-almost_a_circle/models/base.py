#!/usr/bin/python3

class Base:
	"""Private class attribute to keep track of the number of objects"""
	__nb_objects = 0

	# Constructor method to initialize the object
	def __init__(self, id=None):
		# Check if id argument is provided
		if not id == None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
