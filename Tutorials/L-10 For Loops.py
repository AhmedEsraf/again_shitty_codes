# structure: for item in 'Python'

for letters in 'Python': # prints all the values in 'Python'
    print(letters)

List = ['mosh','josh','matilda']

for items in List: # prints all the items of list
    print(items)

for numbers in range(1,11): # also works with range
    print(numbers)

for gap_numbers in range(2,20,2): # see the result to find
    print(gap_numbers)

# Exercise-1: calculate summation using for loop

price_list = [10,200,300,1000]
total_price = 0

for price in price_list:
    total_price += price

print(total_price)