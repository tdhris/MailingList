import List
import assist_functions

def process_input(command):
	if command == 'exit':
		assist_functions.greet_user()

	elif command == 'help':
		assist_functions.print_list_of_commands()

	elif command == 'show_lists':
		pass

	elif command.startswith('show_list '):
		pass

	elif command.startswith('add '):
		list_name = assist_functions.get_list_name_from_command(command)
		new_person = add_person()
		assist_functions.add_person_to_list_file(new_person, list_name)

	elif command.startswith('create '):
		list_name = assist_functions.get_arguments(command, 1)
		print("{} was created".format(list_name))
		new_list = List.List(list_name)

	elif command.startswith("update_subscriber"):
		pass

	elif command.startswith("remove_subscriber"):
		pass

	elif command.startswith("update "):
		pass

	elif command.startswith('search_email'):
		pass

	elif command.startswith('merge_lists'):
		arguments = assist_functions.get_arguments(command, 3)
		first_list, second_list, name_new_list = arguments[0], arguments[1], arguments[2]
		merge_lists(first_list, second_list, name_new_list)

	elif command.startswith('export'):
		list_index = assist_functions.get_arguments(command, 1)
		assist_functions.export(list_index)


	elif command.startswith("import"):
		pass

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

	while True:
		command = take_input()
		process_input(command)


if __name__ == '__main__':
	main()
