# returns a value to the user

def square(number):
    return number*number


# here we returned a value of number*number to the square function
# and now we need to store it


num = int(input('Enter a number: '))
result = square(num) # basically stores the returned function in a variale with that specific arguement
print(result)

# or use
print(square(num)) # or just print the returned value using print()


# or
def sq(num):
    print(num * num)  # without return function


number = int(input('Enter a number: '))
sq(number)

# by default, all functions return none.
