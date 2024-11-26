# We use classes to define new types

# class names are always wriiten in Capitals and no UnderScore in Between
# Like: email_addresss is wrong whereas , EmailAddress is correct

class Point: # creates a new Point class
    def move(self):
        print('Move') # adds new function for the Point class

    def draw(self):
        print('Draw') # adds new function for the Point class


point1 = Point() # defines point1 variable as Point class
point1.x = 20 # adds atrribute to point1 variable
point1.y = 30
print(point1.x, point1.y)
point1.move() # does the function of move to this variable