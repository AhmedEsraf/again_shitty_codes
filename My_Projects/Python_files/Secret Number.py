''' The Secret number is between 1 and 100.
    Guess the secret number in 7 tries to win.'''

import random
random_number = random.randint(1, 100)
secret_number = random_number
i = 0
tries = 1

print("\nThe Secret number is between 1 and 100.\nGuess the secret number in 7 tries to win.\n")



while i < 7:
    guess = int(input(f"Guess the secret number [try number: {tries}] --->"))
    i+= 1
    tries+=1
    if guess == secret_number:
        print("Congrats! You win!")
        break
    elif guess > secret_number:
        print("Your secret number is too high.")
    else:
        print("Your secret number is too low.")
if i == 7 and guess != secret_number:
    print("Sorry! You lose!")


