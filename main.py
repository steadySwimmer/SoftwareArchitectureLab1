from Book import *
from User import *

u = User('Tim', 43)

b = Book('TAe', 'ere', 12)

print (b)

b.owner = u
print (b.owner)

print (b)

