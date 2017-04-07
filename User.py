""" Implementation of User class """

class User:
    """ Describes all properties of library user.

    Attributes:
        __book_list(lst): Contains books are taken by a particular user.
    """

    def __init__(self, user_name, age):
        """ Initialize User class.

        Args:
            user_name(str): User name; can be an arbitrary sequence of characters.
            age(int): User's age; must be in (0..100).
        """
        self.user_name = user_name
        self.age = age
        self.__book_list = []
        super().__init__()

    @property
    def user_name(self):
        """ str: Contains a name of a particular user """
        return self.__user_name

    @property
    def age(self):
        """ int: Contains an age of  a particular user, must be in range(1, 100) """
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            raise Exception("Age must be value between 1 and 99")

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    def take_book(self, book):
        """ Function add book to user's book list.

        Args:
            book(:obj:Book): Information about a book that user take.
        """
        self.__book_list.append(book)

    def return_book(self, title):
        """ Remove book from the book list.

        Args:
            title(str): Book's title.
        """
        self.__book_list = [book for book in self.__book_list if book.book_name != title]

    def __str__(self):
        return "{}, age: {}".format(self.user_name, self.age)


