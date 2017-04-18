"""Implementation of View class."""


class View:
	"""The class is responsible for information output.
	Class consist of static methods, due to the absent
	of it initialization.
	"""

	@staticmethod
	def separator_line():
		print ("\n|-----------------------------------------------|\n")

	@staticmethod
	def main_menu():
		View.separator_line()
		print ("Enter a number to choose the option")
		print ("1. Choose user.")
		print ("2. Create user.")
		print ("3. List of user.")
		print ("4. Remove user.")
		print ("5. Choose book.")
		print ("6. Create book.") 
		print ("7. List of books.")
		print ("8. Remove book.")
		print ("9. Exit.")
		View.separator_line()
		pass

	@staticmethod
	def user_create():
		View.separator_line()
		print ("Enter the information about new user\n.")
		pass

	@staticmethod
	def book_create():
		View.separator_line()
		print ("Enter the information about new book\n.")
		pass

	@staticmethod
	def take_book():
		View.separator_line()
		print ("Take a book from the list. The library has only one copy of book.\n\
				So book can be taken only once or you should wait when someone will\n\
				return it.")
		pass

	@staticmethod
	def return_book():
		View.separator_line()
		print ("Choose a book from your list, which you wanna return.")
		pass

	@staticmethod
	def print_users(user_list):
		View.separator_line()
		for user in user_list:
			print ( ", ".join(map(lambda user: user + ': ' + str(user_list['age']))) )

		View.separator_line()
		pass

	@staticmethod
	def print_books(book_list):
		pass

	@staticmethod
	def print_one_user(user):
		pass

	@staticmethod
	def print_one_book(book):
		pass

	@staticmethod
	def print_user_books(user):
		pass

	@staticmethod
	def wrong_option():
		print ("No current option.")

	@staticmethod
	def exit_message():
		print ("Bye, bye))")
