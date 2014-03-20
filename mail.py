import List
from assist_functions import greet_user, print_list_of_commands, get_list_name_from_command, add_person_to_list_file, get_arguments, merge_lists, export

def process_input(command):
	if command == 'exit':
		greet_user()

	elif command == 'help':
		print_list_of_commands()

	elif command == 'show_lists':
		pass

	elif command.startswith('show_list '):
		pass

	elif command.startswith('add '):
		list_name = get_list_name_from_command(command)
		new_person = add_person()
		add_person_to_list_file(new_person, list_name)

	elif command.startswith('create '):
		list_name = get_arguments(command, 1)
		print("{} was created".format(list_name))
		new_list = List.List(list_name)

	elif command.startswith('search_email'):
		pass

	elif command.startswith('merge_lists'):
		arguments = get_arguments(command, 3)
		first_list, second_list, name_new_list = arguments[0], arguments[1], arguments[2]
		merge_lists(first_list, second_list, name_new_list)

	elif command.startswith('export'):
		list_index = get_arguments(command, 1)
		export(list_index)
		
	else:
		pass


def take_input():
	command = input(">> ")
	return command

def add_person():
	name = input("Enter name >> ")
	email = input("Enter email >>")
	new_person = List.Person(name, email)
	return new_person

def main():
	greet_user()
	command = take_input()

	while True:
		process_input(command)
		command = take_input()


if __name__ == '__main__':
	main()