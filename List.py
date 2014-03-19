import json

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
		list_filename = get_valid_filename(self.list_name)
		open(list_filename, "w").close()

	def add_list_to_archive(self):
		index = get_index_of_new_line(self.archive_filename)
		identifier = get_identifier(index)
		entry = set_entry([identifier, self.list_name])
		write_to_file(self.archive_filename, entry, "a")



def get_valid_filename(list_name):
	name = remove_spaces(list_name)
	return add_txt_extention(name)


def remove_spaces(name):
	return name.replace(' ', '_')


def add_txt_extention(filename):
	return filename + '.txt'


def get_index_of_new_line(filename):
	file = open(filename, "r")
	index = 0
	for line in file:
		index += 1
	file.close()
	return index + 1


def get_identifier(index):
	return '[' + str(index) + ']'


def set_entry(list_of_elements):
	separator = ' '
	entry = separator.join(list_of_elements) + '\n'
	return entry

def get_arguments(command, number_of_arguments):
	arguments = [arg.rstrip('\n') for arg in command.split(' ', number_of_arguments)[1:]]
	if len(arguments) == 1:
		return str(arguments[0])
	else:
		return arguments

def write_to_file(filename, entry, mode):
	file = open(filename, mode)
	file.write(entry)
	file.close()


