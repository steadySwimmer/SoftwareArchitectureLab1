""" this is model"""

import pickle
import datetime

class User:
    """ Describes all properties of library user"""

    def __init__(self, user_name, age):
        self.user_name = user_name
        self.age = age
        self.__book_list = []

    @property
    def user_name(self):
        """ Return user name """
        return self.__user_name

    @property
    def age(self):
        """ Return user's age """
        return self.__age

    @age.setter
    def age(self, age):
        """ Set user's age """
        if age > 0 and age < 100:
            self.__age = age
        else:
            raise Exception("Age must be value between 1 and 99")

    @user_name.setter
    def user_name(self, user_name):
        """ Set user name """
        self.__user_name = user_name

    def take_book(self, book):
        """ Function add book to user's book list """
        self.__book_list.append(book)

