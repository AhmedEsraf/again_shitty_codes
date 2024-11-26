# Strings

course1 = "Python's course for Beginners" # Use Double quote to use apostrophe in sentence
print(course1)

course2 = 'Python course for "Beginners"' # Use single quote to us use Double quote in sentence
print(course2)

course3 = '''Hi, lol!
I'm writing a sentence where both "Double Quotes" and "Single Quote" is necessary.
So, I have to use "Triple Quotes" to properly write this string.
'''

print(course3)

# Indexing


print(course1[0])
print(course1[-1]) # to get the index of the last character
print(course1[0:6]) # to get a range of index and it ignores last index in given range
           # in this case the 6th index
print(course1[8:]) # if we don't provide ending range then it will print all the index from starting index to end
print(course1[:16]) # if no starting index is given ,it auto assumes it  is 0

name = 'Jennifer'
print(name[1:-1])

First_name = ("Ahmed")
last_name = ("Esraf")
message = First_name + " [" + last_name + '] is a coder.' # This is not ideal to print this kind of message

print(message)\

# Formated Strings

msg = f'{First_name} [{last_name}] is a coder.' # Use f at first to format string and {} to place values
print(msg) # {} are placeholders that holds the values here

