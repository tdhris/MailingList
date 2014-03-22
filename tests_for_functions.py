import sys
import assist_functions
import mail
import List
import unittest
import json


class FunctionsTests(unittest.TestCase):

	def test_remove_spaces(self):
		
		self.name = "a test with spaces"
		self.assertEqual("a_test_with_spaces", assist_functions.remove_spaces(self.name))

	def test_add_txt_extention(self):
		self.name = "I have no extention"
		self.assertEqual("I have no extention.txt", assist_functions.add_txt_extention(self.name))

	def test_get_valid_filename(self):
		self.name = "Test several"
		self.assertEqual("Test_several.txt", assist_functions.get_valid_filename(self.name))

	def test_get_identifier(self):
		self.name = "index"
		self.assertEqual("[index]",assist_functions.get_identifier(self.name))

	def test_set_entry(self):
		self.name = ["this","is","a","list"]
		self.assertEqual("this is a list\n", assist_functions.set_entry(self.name))

	def test_get_arguments(self):
		command = "command New List"
		self.assertEqual("New List", assist_functions.get_arguments(command, 1))
		command_2 = "command 2 3 LalaList"
		self.assertEqual(["2" , "3", "LalaList"], assist_functions.get_arguments(command_2, 3))

	def test_get_list_name_from_command(self):
		pass


		"""	def get_list_name_from_command(command):
			default_number_arguments = 1
			list_index = get_arguments(command, default_number_arguments)
			list_name = get_list_from_archive(list_index)
			return list_name"""


if __name__ == '__main__':
    unittest.main()