import json
import sys

class Person:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def search_email(self, email):
		

class List:
	def __init__(self, list_name, identifier):
		self.list_name = list_name
		self.identifier = identifier
		self.create_list_file()
		self.add_list_to_archive()

	def show_lists(self):
		
		def read(self):
			if(sys.argv) > 1:
				file = open("lists.txt", "r")
				print(file.read())
			else:
				print "No lists!"
		
		for arg in range(1,len(sys.argv)):
		read(sys.argv[arg])

		

	def show_list(self,identifier):
		self.identifier = sys.argv

		def read(self):
			if(sys.argv) > 1:
				file = open("lists.txt", "r")
				print(file.read())
			else:
				print "No lists!"
		
		for arg in range(1,len(sys.argv)):
		read(sys.argv[arg])


