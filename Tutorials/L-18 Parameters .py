def greet_user(name):
    print(f'Hello there,{name}!')
    print('Welcome aboard!')


print('Start')
user_name= input('Enter your name: ')
greet_user(user_name)
print('End')

'''Making a parameter allows you to re-use your codes with different inputs.
basically making your own python functions.
Parameters basically works as placeholders to receive informations. 
They are not Arguments which means Absolute information'''