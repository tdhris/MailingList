import List
import assist_functions

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
		list_name = assist_functions.get_list_name_from_command(command)
		new_person = add_person()
		add_person_to_list_file(new_person, list_name)

	elif command.startswith('create '):
		list_name = assist_functions.get_arguments(command, 1)
		print("{} was created".format(list_name))
		new_list = List.List(list_name)

	elif command.startswith('search_email'):
		pass

	elif command.startswith('merge_lists'):
		arguments = assist_functions.get_arguments(command, 3)
		first_list, second_list, name_new_list = arguments[0], arguments[1], arguments[2]
		merge_lists(first_list, second_list, name_new_list)

	elif command.startswith('export'):
		list_index = assist_functions.get_arguments(command, 1)
		assist_functions.export(list_index)
		
update_subscriber <unique_list_identifier> <unique_name_identifier>
* remove_subscriber <unique_list_identifier> <unique_name_identifier>
 update <unique_list_identifier>  <new_list_name>
 "import <filename"

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
	assist_functions.greet_user()
	command = take_input()

	while True:
		process_input(command)
		command = take_input()


if __name__ == '__main__':
	main()