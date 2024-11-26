# we use modules to organise our codes into multples files

import modulestest
print(modulestest.lbs_to_kg(70))
# we just imported the functions from another file to work in this file


# We can also import specific functions from that module
from modulestest import lbs_to_kg
print(lbs_to_kg(70))


# Exercise: Make find_max function in utils folder and import it to this file
# and use that function to find the maximum number
from utils import find_max

list = [1,5,7,99,456]
print(find_max(list))

# we can also import files from different folder like this

import Tutorials.utils # this wont work as it it the same folder but will works in different folders
print(Tutorials.utils.find_max(list))

# but using from statement is better in this case

from Tutorials import utils
print(utils.find_max(list))