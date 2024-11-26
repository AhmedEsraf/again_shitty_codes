# dictionaries consist of two parts: key and pairs

dict = {'name':'Ahmed',
        'age':20,
        'verified':True}
# Each key should be unique in a dictionary just like a real dictionary

print(type(dict))

print(dict['age']) # prints value of a certain key

# also it is case-sensitive

print(dict.get('age')) # doesnt give error if key doesnt exist
print(dict.get('date')) # gives none as output
print(dict.get('date','1st January')) # get() can give a default value if key doesnt exist

dict['name'] = 'Esraf' # values can be modified
print(dict)

dict['likes'] = 'video games' # adds new key with value
print(dict)

# Exercise: number translator

number = input('Enter a number: ')

num_dict = {'0':'zero',
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '5':'five',
            '6':'six',
            '7':'seven',
            '8':'eight',
            '9':'nine',}
output = ''
for char in number:
    output += num_dict.get(char) + ' '

print(output)