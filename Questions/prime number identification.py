def find_prime():
    num = int(input('Type Your Number:'))
    if num % 2 == 0:
        print('Not Prime')
    elif num % 3 == 0:
        print('Not Prime')
    elif num % 5 == 0:
        print('Not Prime')
    elif num % 7 == 0:
        print('Not Prime')
    elif num % 11 == 0:
        print('Not Prime')
    elif num % 13 == 0:
        print('Not Prime')
    else:
        print('Prime')
    return 0

find_prime()
