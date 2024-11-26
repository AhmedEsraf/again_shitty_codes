class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y # self refers to the current object
    def move(self):
        print('Move')
    def draw(self):
        print('Draw')

point1 = Point(10, 2)
print(point1.x, point1.y)


# Exercise: Adding a class called 'Person' that has name attribute and talk() method

class Person:
    def __init__(self, name): # initializes atrributes to be given to this class
        self.name = name # this line is very important
    def talk(self):
        print('Hello , I am ' + self.name + '.')

person1 = Person('Ahmed')
print(person1.name)
person1.talk()
