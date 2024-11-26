# The position doesnt matter for keyword arguments

def greet_user(first_name, last_name):
    print(f'Hello there, {first_name} {last_name}!')
    print('Welcome aboard!')


print('Start')
greet_user(last_name='Esraf',first_name='Ahmed')
print('End')

'''Here the red texts (first_name and lastname ) in second block of codes
 are keyword arguements. their positions dont matter as they are already defind in the 
 greet_user function.
 Basically its giving arguemts for those specific parameters'''

# They are very useful in number arguments ,like:

def total_cost(shippingcost,tax,delivery):
    return shippingcost+tax+delivery
    # ignore the return statement for now
# learn about return statement in next lession


print('start')
print(total_cost(shippingcost=1000,tax=50,delivery=10))
print('end')

# here we can see what arguement is for what
# Use Keyword Arguements after positional arguements

