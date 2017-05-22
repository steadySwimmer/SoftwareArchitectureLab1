""" Module for serialization using JSON format """

import json
from User import User
from Book import Book

def js_default(obj):
    if isinstance(obj, Book):
        return dict([('book_name', obj.book_name), ('book_author', obj.book_author), \
                    ('book_year', obj.book_year), ('rates', obj._rates())])
    return obj.__dict__


def decode_json(dct):
    user = User(dct['_User__user_name'], dct['_User__age'])
    for element in dct['_User__book_list']:
        book = Book(element['book_name'], element['book_author'], element['book_year'], element['rates'])
        book.owner = user
        user.take_book(book)
    return user

def jload(file_obj):
    return json.load(file_obj, ho)

def jdump():
    pass

