import json
import assist_functions

class Person:
	def __init__(self, name, email):
		self.name = name
		self.email = email


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