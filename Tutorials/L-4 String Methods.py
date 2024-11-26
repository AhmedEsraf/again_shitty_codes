# String methods


course = 'Python for Beginners'
print(len(course)) # use len() to see the length of the string

# Uppercase
print(course.upper())

# Lowercase
print(course.lower())

# Finding characters
print(course.find('P')) # case-sensitive
print(course.find('Beginners'))

# Replacing Characters
print(course.replace('Beginners', 'Hablus')) # also case-sensitive

# To Find characters in String using Boolean
print('Python' in course)

# To make a string look like Title
print(course.title())