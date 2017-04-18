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
				mode = int(input("Choose: "))
			except ValueError:
				View.wrong_option()
				mode = 0

			if mode == 1:
				View.print_users(self.model.user_list)
				View.main_menu()
			elif mode == 2:
				self.create_user_manager()
				View.main_menu()
			elif mode == 3:
				View.main_menu()
			elif mode == 4:
				View.main_menu()
			elif mode == 5:
				View.print_books(self.model.book_list)
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


