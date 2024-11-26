list = [1,2,3,4,5]

list.append(20) # adds new item to the list
print(list)

list.insert(1,'lol') # inserts new item in list with index
print(list)

list.remove('lol') # removes an item
print(list)

list.clear() # removes all the items from the list
print(list)

list = [1,2,3,4,5,3,3]

list.pop() # removes the last item from the list
print(list)

print(list.index(1)) # prints the index of an item

print('lol' in list) # checks the existence of an item

print(list.count(3)) # checks the count of an item

list.sort() # sorts the list in ascending order
print(list)

list.reverse() # reverses the list
print(list)

copied_list = list.copy() # copies a list
print(copied_list)

# Exercise: remove all the duplicates from a list

list = [1,2,3,4,5,3,3,1,5]
uniques = []

for number in list:
    if number not in uniques:
        uniques.append(number)

print(uniques)