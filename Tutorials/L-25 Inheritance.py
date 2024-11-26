# Inheritance is a mechanism for re-using codes
# it inherits code from a mother class and gives to another classes

class Mammal:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(self.name +" walks.")


class Dog(Mammal): # the dog class now inherits the functions of Mammal class
    pass # needs to write pass to inherit


class Cat(Mammal):  # same as dog class
    def meow(self):
        print(self.name +" meows.") # you can also add extra functions to inherited classes

# so we dont need pas statement


jenny = Cat('Jenny')
jenny.walk()
jenny.meow()
