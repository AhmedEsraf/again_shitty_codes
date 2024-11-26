list = ['apple','banana','cherry','date']
print(type(list))

print(list[0]) # prints the first item
print(list[-1]) # prints the last item
print(list[1:3]) # prints a range of items

list[0] = 'adam' # changes list items
print(list)

# EXercise-1: write a program to find the biggest number in a list

list1 = [1,5,55,999,23]
max = list1[0]
for i in list1:
    if i > max:
        max = i
print(max)

# 2D lists or matrics

matrics = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrics[0][1] = 'lol'
print(matrics)
print(matrics[0][1]) # row and column

for row in matrics: # shows all the elements in matrics
    for elem in row:
        print(elem)
