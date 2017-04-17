""" Implementation of Model class """

import pickle
from User import User
from Book import Book


class Model:
    """ Class Model controls all operation on users and books in the library.

    Attributes:
        __users_list(list): List of library users.
        __books_list(list): List of books available in the library.
    """

    def __init__(self, filename):
        """ Initialize Model class

        Args:
            filename(str): Set name of the file which is used to upload
                information about library.
        """
        self.__users_list = []
        self.__books_list = []
        self.load(filename)
        super().__init__()


    @property
    def user_list(self):
        """ list: Contains the list of library users. """
        return self.__users_list


    @property
    def book_list(self):
        """ list: Contains the list of books in a library. """
        return self.__books_list


    def create_user(self, username, age):
        """ Method  create user and add to user list.

        Args:
            username(str): Library user's name.
            age(int): User's age.
        """
        if self._is_username_exists(username):
            raise Exception("[ERROR]::The user already exists.")
        self.__users_list.append(User(username, age))


    def remove_user(self, username):
        """ Removes user form user list.

        Args:
            username(str): The name of the deleted user.
        Raises:
            Exception: if user with given username does not exist.
        """
        if not self._is_username_exists(username):
            raise Exception("[ERROR]::There is no user with such name.")
        self.__users_list = [user for user in self.__users_list if user.user_name != username]


    def add_book(self, title, author, year=None):
        """ Add new book to the library.

        Args:
            title(str): Book's title.
            author(str): Book's author.
            year(int, optional): The year when book was published
        """
        self.__books_list.append(Book(title, author, year))


    def remove_book(self, title):
        """ Removes book from the library.

        Args:
            title(str): Book's title.
        Raises:
            Exception: if book with given title does not exist.
        """
        if not self._is_book_title_exists(title):
            raise Exception("[ERROR]::There is no book with shuch title.")
        self.__books_list = [book for book in self.__books_list if book.book_name != title]


    def take_book(self, username, book_title):
        """ Adds the book to the user's book list.

        Args:
            username(str): User's name.
            book_title(str): Book's title.
        Raises:
            Exception: if user with given username does not exist
                        or book with given title does not exist.
        """
        if not (self._is_book_title_exists(book_title) \
        and self._is_username_exists(username)):
            raise Exception("[ERROR]::There is no such user or book.")

        book_index = self.__books_list.index([item for item in self.__books_list \
                                             if item.book_name == book_title][0])
        self.__books_list[book_index].owner = username
        user_index = self.__users_list.index([item for item in self.__users_list \
                                             if item.user_name == username][0])
        self.__users_list[user_index].take_book(self.__books_list[book_index])


    def return_book(self, username, book_title):
        """ Returns book back to the library.

        Args:
            username(str): User's name.
            book_title(str): Book's title.
        Raises:
            Exception: if user with given username does not exist
                        or book with given title does not exist.
        """
        if not (self._is_book_title_exists(book_title) \
        and self._is_username_exists(username)):
            raise Exception("[ERROR]::There is no such user or book.")

        book_index = self.__books_list.index([item for item in self.__books_list \
                                             if item.book_name == book_title][0])
        self.__books_list[book_index].owner = None
        user_index = self.__users_list.index([item for item in self.__users_list \
                                             if item.user_name == username][0])
        self.__users_list[user_index].return_book(book_title)


    def load(self, filename):
        """ Load information about library users and books

        Args:
            filename(str): Set name of the file which is used to upload
                information about library.
        """
        try:
            with open(filename, 'rb') as source:
                self.__users_list, self.__books_list = pickle.load(source)
        except OSError:
            self.__users_list = []
            self.__books_list = []


    def save(self, filename):
        """ Save information about library in text file.

        Args:
            filename(str): Set name of the file which is used to upload
                information about library.
        """
        with open(filename, 'wb') as target_file:
            pickle.dump([self.__users_list, self.__books_list], target_file)

    def _is_username_exists(self, username):
        user_name = [user for user in self.__users_list if user.user_name == username]
        return True if user_name else False

    def _is_book_title_exists(self, book_title):
        title = [book for book in self.__books_list if book.book_name == book_title]
        return True if title else False
