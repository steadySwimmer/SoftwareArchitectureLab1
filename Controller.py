from View import View
from Model import Model
from random import *

class Controller:

	@staticmethod
	def start():
		mode = 0
		View.main_menu()

		while mode != 9:
			try: 
				mode = int(input("Choose "))
			except ValueError:
				View.wrong_option()
				mode = 0

			if mode == 1:
				View.main_menu()
			elif mode == 2:
				View.main_menu()
			elif mode == 3:
				View.main_menu()
			elif mode == 4:
				View.main_menu()
			elif mode == 5:
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
