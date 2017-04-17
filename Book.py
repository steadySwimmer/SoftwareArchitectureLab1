import functools
from User import *


class Book:
    """ The class represents the enity of a real world book. """

    def __init__(self, book_name, book_author, book_year=None):
        """ Initializer of Book class
            Args:
                book_name:(str): The name of the book
                book_author:(str): The name of author of the current book
                book_year:(int, optional): The year when book was published

            Private attribute:
                rates:(list): The list which store all rates
                that were ever setted. Stored to compute the book's rate.
        """
        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
        self.rate = None
        self.owner = None
        self.__rates = []

    def __str__(self):
        if hasattr(self, 'owner'):
            return "Book name: " + self.book_name + "; Author: " + self.book_author + ";\nBook owner: (" + str(self.owner) + ")"
        else:
            return "Book name: " + self.book_name + "; Author: " + self.book_author

    @property
    def book_name(self):
        """str: Property that stores the book name
            of the current book.
        """
        return self.__book_name

    @book_name.setter
    def book_name(self, book_name):
        self.__book_name = book_name

    @property
    def book_author(self):
        """str: Property that stores the book author"""
        return self.__book_author

    @book_author.setter
    def book_author(self, book_author):
        self.__book_author = book_author

    @property
    def book_year(self):
        """int: Property that stores the year when the book was published. """
        return self.__book_year

    @book_year.setter
    def book_year(self, book_year):
        self.__book_year = book_year

    @property
    def book_rate(self):
        """float: The average rate of the book.
            Computing due to all rates that were ever setted
            to the current book.
        """
        return self.__book_rate

    @book_rate.setter
    def book_rate(self, book_rate):
        """ float: The book rate setter is computing the rate
            of book taking the sum of list with already
            setted rates and divides it on the current
            length of rates stored in rates list and plus
            one due to one added in this setter.
        """
        if (book_rate >= 0.0 and book_rate <= 5.0):
            self.__book_rate = (reduce(lambda x, y: x + y, self.__rates) + book_rate) / (len(self.__rates) + 1)
            self.__book_rate.append(book_rate)
        else:
            raise Exception('Rate value must be between 0.0 and 5.0')

    @property
    def owner(self):
        """User: The attribute of type User, that is storing
                the user, who took the book.
        """
        return self.__owner

    @owner.setter
    def owner(self, owner):
        """ Setter checks if new value is the object of type User
        """
        if isinstance(owner, User):
            self.__owner = owner
