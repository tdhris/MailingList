import json

class Person:
	def __init__(self, name, email):
		self.name = name
		self.email = email


class List:
	def __init__(self, list_name):
		self.list_name = list_name
		self.create_list_file()
		self.add_list_to_archive()