from Controller import Controller
from Model import Model

model = Model('storage')

model.load()

model.add_book('Harry', 'Kate', 1956)

print (model._users_list)

model.save()