# python has alot of coommon packages for common tasks like this one.

import random

for i in range(3): # using this for loop we just generated totally random numbers 3 times
    print(random.random())

for i in range(3): # using this for loop we just generated random integers from 1 to 100 ,3 times
    print(random.randint(1,100))

members = ['John','Mary','Mark','Wade','Bob']
for i in range(3): # selects a random leader from members lists 3 times
    print('Our Leader is ' + random.choice(members))

#  Exercise: make a class 'dice' where it random gives a tuple consisting two dice rolls


class Dice:
    def roll(self):
        first_number = random.randint(1,6)
        second_number = random.randint(1,6)
        tuple = (first_number, second_number)
        return tuple


Chokka = Dice()
print(Chokka.roll())
