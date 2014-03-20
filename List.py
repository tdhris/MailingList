import json
import assist_functions

class Person:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def change_name(self, new_name):
		self.name = new_name

	def change_email(self, new_email):
		self.email = new_email

class List:
	archive_filename = 'archive.txt'

	def __init__(self, list_name):
		self.list_name = list_name
		self.create_list_file()
		self.add_list_to_archive()

	def create_list_file(self):
		list_filename = assist_functions.get_valid_filename(self.list_name)
		open(list_filename, "w").close()

	def add_list_to_archive(self):
		index = assist_functions.get_index_of_new_line(self.archive_filename)
		identifier = assist_functions.get_identifier(index)
		entry = assist_functions.set_entry([identifier, self.list_name])
		assist_functions.write_to_file(self.archive_filename, entry, "a")

	def remove_list_from_archive(self, list_index):
		identifier = assist_functions.get_identifier(list_index)
		archive = open("archive.txt", "r")
		content = archive.read().split('\n')
		content.remove(content[int(list_index) - 1])
		archive.close()
		archive = open("archive.txt", "w")
		archive.write(''.join(content))


