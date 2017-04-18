from View import View
from Model import Model
from random import *

class Controller:

	def __init__(self, main_model):
		self.model = main_model
		super().__init__()

	def start(self):
		mode = 0
		View.main_menu()

		while mode != 9:
			try: 
				mode = int(input("Choose option: "))
			except ValueError:
				View.wrong_option()
				mode = 0

			if mode == 1:
				View.print_users(self.model.user_list)
				self.take_return_book_option()
				View.main_menu()
			elif mode == 2:
				self.create_user_manager()
				View.main_menu()
			elif mode == 3:
				View.detailed_print_users(self.model.user_list)
				View.main_menu()
			elif mode == 4:
				View.print_users(self.model.user_list)
				self.delete_user_manager()
				View.main_menu()
			elif mode == 5:
				View.print_books(self.model.book_list)
				self.set_book_rate_manager()
				View.main_menu()
			elif mode == 6:
				View.main_menu()
			elif mode == 7:
				View.main_menu()
			elif mode == 8:
				View.main_menu()
			elif mode == 9:
				View.exit_message()
			elif mode not in range(1, 10):
				View.main_menu()

	def create_user_manager(self):
		user_name = None
		user_age = 0
		try:
			user_name = str(input("Enter user name: "))
			user_age = int(input("Enter user age: "))
		except ValueError:
			View.wrong_input()
			return

		self.model.create_user(user_name, user_age)
		View.success_user_create_message()
		return

	def take_return_book_option(self):
		user_number = 0
		try:
			user_number = int(input("Enter user number: "))
		except ValueError:
			View.wrong_input()
			return
		if (user_number not in range(1, len(self.model.user_list) + 1)):
			View.wrong_input()
			return

		View.take_return_book()
		option = 0
		try:
			option = int(input("Choose option: "))
		except ValueError:
			View.wrong_input()
			return

		if option == 1:
			self.take_book_manager(self.model.user_list[user_number - 1])
		elif option == 2:
			self.return_book_manager(self.model.user_list[user_number - 1])
		else:
			View.wrong_input()
			return


	''' Take and return book procces '''
	def take_book_manager(self, chosen_user):
		number = self.take_return_book_helper(self.model.book_list)
		chosen_user.take_book(self.model.book_list[number])
		return

	def return_book_manager(self, chosen_user):
		number = self.take_return_book_helper(chosen_user.book_list)
		book = chosen_user.book_list[number]
		chosen_user.return_book(book.book_name)

	def take_return_book_helper(self, book_list):
		View.print_books(book_list)
		book_number = 0
		try:
			book_number = int(input("Enter book number: "))
		except ValueError:
			View.wrong_input()

		if (book_number not in range(1, len(book_list) + 1)):
			View.wrong_input()
			return
		return book_number - 1

	def delete_user_manager(self):
		user_number = 0
		try:
			user_number = int(input("Enter user number: "))
		except ValueError:
			View.wrong_input()
			return
		if (user_number not in range(1, len(self.model.user_list) + 1)):
			View.wrong_input()
			return
		user = self.model.user_list[user_number - 1]
		self.model.remove_user(user.user_name)

	''' Set book rate manager'''
	def set_book_rate_manager(self):
		book_number = 0
		try:
			book_number = int(input("Enter book number: "))
		except ValueError:
			View.wrong_input()
			return

		if (book_number not in range(1, len(self.model.book_list) + 1)):
			View.wrong_input()
			return

		book_rate = 0.0
		try:
			book_rate = float(input("Set book rate: "))
		except ValueError:
			View.wrong_input()
			return

		book = self.model.book_list[book_number - 1]
		book.rate = book_rate
		print ("New book rate {} for Book {}".format(book.rate, book))

