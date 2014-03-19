import assist_functions
import List


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
		pass

	elif command.startswith('create '):
		pass

	elif command.startswith('search_email'):
		pass

	elif command.startswith('merge_lists'):
		pass

	elif command.startswith('export'):
		pass
		
	else:
		pass


def take_input():
	command = input(">> ")
	return command


def main():
	assist_functions.greet_user()
	command = take_input()

	while True:
		process_input(command)
		command = take_input()


if __name__ == '__main__':
	main()