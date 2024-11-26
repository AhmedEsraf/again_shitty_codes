# Exercise-1: Generating co-ordinates

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

# Exercise-2: Generating an 'F' shape using for inner/nested loop with 'x' letter

numbers = [5,2,5,2,2]

for num in numbers:
    print('x' * num)
print('\n')
# or

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

