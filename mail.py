import List


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
		pass

	elif command.startswith('create '):
		list_name = List.get_arguments(command, 1)
		print("{} was created".format(list_name))
		new_list = List.List(list_name)

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

def greet_user():
	print("Hello Stranger! This is a cutting-edge, console-based mail-list!\nType help, to see a list of commands.")

def print_list_of_commands():
	file = open("list_of_commands.txt", "r")
	list_of_commands = file.read()
	file.close()
	print(list_of_commands)


def main():
	greet_user()
	command = take_input()

	while True:
		process_input(command)
		command = take_input()


if __name__ == '__main__':
	main()