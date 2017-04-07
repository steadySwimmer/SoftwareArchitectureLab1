""" Implementation of Model class """

import pickle
from User import User
from Book import Book


class Model:
    """ Class Model controls all operation on users and books in the library.

    Attributes:
        __users_list(list): list of library users.
        __books_list(list): list of books available in the library.
    """

    def __init__(self, filename):
        """ Initialize Model class

        Args:
            filename(str): set name of the file which is used to upload
                information about library.
        """
        self.__users_list = []
        self.__books_list = []
        self.load(filename)
        super().__init__()


    def create_user(self, username, age):
        pass

    def remove_user(self, username):
        pass

    def add_book(self, title, author=None, year=None):
        pass

    def remove_book(self, title):
        pass

    def load(self, filename):
        """ Load information about library users and books

        Args:
            filename(str): set name of the file which is used to upload
                information about library.
        Raises:
            OSError: if not found file or have problems with reading it.
        """
        try:
            with open(filename, 'rb') as source:
                self.__users_list, self.__books_list = pickle.load(source)
        except OSError as err:
            self.__users_list = []
            self.__books_list = []
            raise Exception("[ERROR]::" + str(err))


    def save(self, filename):
        """ Save information about library in text file.

        Args:
            filename(str): set name of the file which is used to upload
                information about library.
        """
        with open(filename, 'wb') as target_file:
            pickle.dump([self.__users_list, self.__books_list], target_file)

