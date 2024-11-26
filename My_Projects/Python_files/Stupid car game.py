# Making a car game where we input the car to drive it

print('start - to start the car \n stop - to stop the car \n speed - to speed up \n quit - to quit the game')
started = False
speed = 0
kmh = 0
# use .strip().lower() to use capitalization and lower also
while True:

    options = input('Your input: ').strip().lower()
    if options == 'start'and started == False:
        started = True
        print('Your car has started....')
    elif options == 'start' and started == True:
        print('Sorry! Your car is already started....')
    elif options == 'stop' and started == True:
        started = False
        print('Your car has stopped....')
    elif options == 'stop' and started == False:
        print('Sorry! Your car is already stopped....')
    elif options == 'quit':
        print('Thanks for playing!')
        break
    elif options == 'speed' and started == True:
        speed += 1
        kmh += 40
        print(f'Your car sped up! Average speed : {kmh} km/h')
        if speed == 4:
            print("Oh no! You crashed.")
            break
    elif options == 'speed' and started == False:
        print('Sorry! But You did not start your car.')
    else:
        print('Invalid option??!?!?')

