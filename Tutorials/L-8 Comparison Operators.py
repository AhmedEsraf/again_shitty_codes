# Exercise-1:

''' if temperature is greater than 30
    it Is a hot day.
otherwise, if it Is less than 10,
    it Is a cold day.
otherwise
    it Is neither hot nor cold.'''

temperature = int(input('Enter temperature: '))

if temperature >= 30: # greater than operator
    print('It is a hot day!')
elif temperature <= 10: # less than operator
    print('It is a cold day!')
else:
    print('It is neither hot nor cold')
print('Be Careful out there!')


# Exercise-2:

''' if name is less than 3 characters long,
    name must be at least 3 characters
otherwise, if it Is more than 50 characters 101;
    name can be a maximum of 50 characters
otherwise,
    name looks good!
'''

name = input('Enter name: ')

if len(name) > 50:
    print('Name too long')
elif len(name) < 3:\
    print('Name too short')
else:
    print('Name looks good!')